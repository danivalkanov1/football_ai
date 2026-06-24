import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from services.players_service import PlayersService
from services.transfers_service import TransfersService
from services.matches_service import MatchesService
from services.standings_service import StandingsService
from repositories.clubs_repo import add_club, list_clubs, find_club_by_name, update_club, delete_club
from repositories.players_repo import list_players_by_club
from ai.ai_service import AIService
from db import fetch_all


class FootballUI:
    def __init__(self):
        self.root = tb.Window(themename="darkly")
        self.root.title("Football AI - Мениджър")
        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)

        self.players_service = PlayersService()
        self.transfers_service = TransfersService()
        self.matches_service = MatchesService()
        self.standings_service = StandingsService()
        self.ai_service = AIService()
        self.current_match_id = None

        self._build_ui()

    def _build_ui(self):
        main = tb.Frame(self.root)
        main.pack(fill=BOTH, expand=YES)

        # Sidebar
        sidebar = tb.Frame(main, width=220, bootstyle="secondary")
        sidebar.pack(side=LEFT, fill=Y)
        sidebar.pack_propagate(False)

        logo = tb.Label(sidebar, text="⚽ Football AI", font=("Segoe UI", 16, "bold"),
                        bootstyle="inverse-secondary", padding=15)
        logo.pack(fill=X)

        self.sections = [
            ("🏠  Начало", "home"),
            ("🏟  Клубове", "clubs"),
            ("👤  Играчи", "players"),
            ("🔄  Трансфери", "transfers"),
            ("📅  Мачове", "matches"),
            ("🏆  Класиране", "standings"),
            ("🤖  Прогноза", "predict"),
        ]

        self.nav_btns = {}
        for text, key in self.sections:
            btn = tb.Button(sidebar, text=text, bootstyle="secondary-outline",
                            command=lambda k=key: self._show_section(k))
            btn.pack(fill=X, padx=10, pady=3)
            self.nav_btns[key] = btn

        # Content
        content = tb.Frame(main)
        content.pack(side=RIGHT, fill=BOTH, expand=YES, padx=20, pady=20)

        self.frames = {}
        for key in ["home", "clubs", "players", "transfers", "matches", "standings", "predict"]:
            f = tb.Frame(content)
            self.frames[key] = f

        self._build_home(self.frames["home"])
        self._build_clubs(self.frames["clubs"])
        self._build_players(self.frames["players"])
        self._build_transfers(self.frames["transfers"])
        self._build_matches(self.frames["matches"])
        self._build_standings(self.frames["standings"])
        self._build_predict(self.frames["predict"])

        self._show_section("home")

    def _show_section(self, key):
        for f in self.frames.values():
            f.pack_forget()
        self.frames[key].pack(fill=BOTH, expand=YES)

        for k, btn in self.nav_btns.items():
            if k == key:
                btn.configure(bootstyle="primary")
            else:
                btn.configure(bootstyle="secondary-outline")

    # ==================== HOME ====================

    def _build_home(self, parent):
        container = tb.Frame(parent)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)

        tb.Label(container, text="⚽ Football AI", font=("Segoe UI", 32, "bold"),
                 bootstyle="primary").pack(pady=(0, 5))
        tb.Label(container, text="Мениджър за футболни лиги", font=("Segoe UI", 14),
                 bootstyle="secondary").pack(pady=(0, 35))

        stats_f = tb.Frame(container)
        stats_f.pack()

        try:
            clubs = list_clubs()
            n_clubs = len(clubs)
        except Exception:
            n_clubs = 0

        cards = [
            ("🏟", "Клубове", str(n_clubs), "Регистрирани клубове"),
            ("👤", "Играчи", "290", "Общо играчи"),
            ("🏆", "Лиги", "2", "Активни лиги"),
        ]

        for i, (icon, title, value, desc) in enumerate(cards):
            card = tb.Frame(stats_f, bootstyle="secondary", padding=20)
            card.grid(row=0, column=i, padx=10, pady=10, ipadx=10)

            tb.Label(card, text=icon, font=("Segoe UI", 36)).pack()
            tb.Label(card, text=title, font=("Segoe UI", 10)).pack()
            tb.Label(card, text=value, font=("Segoe UI", 26, "bold"),
                     bootstyle="primary").pack()
            tb.Label(card, text=desc, font=("Segoe UI", 9)).pack()

        tb.Label(container, text="Използвай навигацията отляво за управление",
                 bootstyle="secondary", font=("Segoe UI", 11)).pack(pady=(30, 0))

    # ==================== CLUBS ====================

    def _build_clubs(self, parent):
        tb.Label(parent, text="🏟  Управление на клубове", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        # Add
        add_f = tb.Frame(parent, bootstyle="secondary", padding=12)
        add_f.pack(fill=X, pady=(0, 10))
        tb.Label(add_f, text="Добави клуб", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        row = tb.Frame(add_f)
        row.pack(fill=X)
        tb.Label(row, text="Име:", width=6).pack(side=LEFT)
        self.club_name_entry = tb.Entry(row, width=25)
        self.club_name_entry.pack(side=LEFT, padx=(0, 15))
        tb.Label(row, text="Град:", width=6).pack(side=LEFT)
        self.club_city_entry = tb.Entry(row, width=20)
        self.club_city_entry.pack(side=LEFT, padx=(0, 15))
        tb.Button(row, text="➕ Добави", bootstyle="primary", command=self._add_club).pack(side=LEFT)

        # List
        list_f = tb.Frame(parent, bootstyle="secondary", padding=12)
        list_f.pack(fill=BOTH, expand=YES)
        tb.Label(list_f, text="Списък с клубове", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        cols = ("id", "name", "city")
        self.clubs_tree = tb.Treeview(list_f, columns=cols, show="headings", height=12,
                                       bootstyle="primary")
        self.clubs_tree.heading("id", text="ID")
        self.clubs_tree.heading("name", text="Име")
        self.clubs_tree.heading("city", text="Град")
        self.clubs_tree.column("id", width=50)
        self.clubs_tree.column("name", width=350)
        self.clubs_tree.column("city", width=250)
        self.clubs_tree.pack(fill=BOTH, expand=YES, pady=(0, 10))

        btn_row = tb.Frame(list_f)
        btn_row.pack(fill=X)
        tb.Button(btn_row, text="✏  Преименувай", bootstyle="info-outline",
                  command=self._rename_club_dialog).pack(side=LEFT, padx=(0, 5))
        tb.Button(btn_row, text="🗑  Изтрий", bootstyle="danger-outline",
                  command=self._delete_club).pack(side=LEFT)

    def _add_club(self):
        name = self.club_name_entry.get().strip()
        city = self.club_city_entry.get().strip() or None
        if not name:
            messagebox.showerror("Грешка", "Името е задължително")
            return
        try:
            cid = add_club(name, city)
            messagebox.showinfo("Успех", f"Клуб добавен с id={cid}")
            self.club_name_entry.delete(0, END)
            self.club_city_entry.delete(0, END)
            self._refresh_clubs()
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _refresh_clubs(self):
        for r in self.clubs_tree.get_children():
            self.clubs_tree.delete(r)
        for c in list_clubs():
            self.clubs_tree.insert("", END, values=(c["id"], c["name"], c.get("city", "")))

    def _selected_club(self):
        sel = self.clubs_tree.selection()
        if not sel:
            messagebox.showerror("Грешка", "Избери клуб от списъка")
            return None
        return self.clubs_tree.item(sel[0])["values"]

    def _rename_club_dialog(self):
        vals = self._selected_club()
        if not vals:
            return
        old_name = vals[1]
        d = RenameDialog(self.root, old_name)
        if d.result:
            try:
                club = find_club_by_name(old_name)
                update_club(club["id"], d.result, club.get("city"))
                self._refresh_clubs()
                messagebox.showinfo("Успех", "Клубът е преименуван")
            except ValueError as e:
                messagebox.showerror("Грешка", str(e))

    def _delete_club(self):
        vals = self._selected_club()
        if not vals:
            return
        if messagebox.askyesno("Потвърди", f"Сигурен ли си, че искаш да изтриеш '{vals[1]}'?"):
            try:
                delete_club(int(vals[0]))
                self._refresh_clubs()
                messagebox.showinfo("Успех", "Клубът е изтрит")
            except ValueError as e:
                messagebox.showerror("Грешка", str(e))

    # ==================== PLAYERS ====================

    def _build_players(self, parent):
        tb.Label(parent, text="👤  Управление на играчи", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        # Add
        add_f = tb.Frame(parent, bootstyle="secondary", padding=12)
        add_f.pack(fill=X, pady=(0, 10))
        tb.Label(add_f, text="Добави играч", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        row = tb.Frame(add_f)
        row.pack(fill=X)
        tb.Label(row, text="Име:", width=8).pack(side=LEFT)
        self.player_name_entry = tb.Entry(row, width=22)
        self.player_name_entry.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="Клуб:", width=5).pack(side=LEFT)
        self.player_club_combo = tb.Combobox(row, width=20, state="readonly")
        self.player_club_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="Поз:", width=4).pack(side=LEFT)
        self.player_pos_combo = tb.Combobox(row, values=["GK", "DF", "MF", "FW"], width=5, state="readonly")
        self.player_pos_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="№:", width=3).pack(side=LEFT)
        self.player_num_entry = tb.Entry(row, width=6)
        self.player_num_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(row, text="➕ Добави", bootstyle="primary", command=self._add_player).pack(side=LEFT)

        # List
        list_f = tb.Frame(parent, bootstyle="secondary", padding=12)
        list_f.pack(fill=BOTH, expand=YES)
        tb.Label(list_f, text="Играчи по клуб", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        filter_row = tb.Frame(list_f)
        filter_row.pack(fill=X, pady=(0, 8))
        tb.Label(filter_row, text="Филтър по клуб:").pack(side=LEFT, padx=(0, 8))
        self.player_filter_combo = tb.Combobox(filter_row, width=25, state="readonly")
        self.player_filter_combo.pack(side=LEFT, padx=(0, 10))
        tb.Button(filter_row, text="🔍 Покажи", bootstyle="info", command=self._refresh_players).pack(side=LEFT)

        cols = ("id", "name", "pos", "num", "status")
        self.players_tree = tb.Treeview(list_f, columns=cols, show="headings", height=14,
                                         bootstyle="primary")
        self.players_tree.heading("id", text="ID")
        self.players_tree.heading("name", text="Име")
        self.players_tree.heading("pos", text="Позиция")
        self.players_tree.heading("num", text="№")
        self.players_tree.heading("status", text="Статус")
        self.players_tree.column("id", width=40)
        self.players_tree.column("name", width=300)
        self.players_tree.column("pos", width=70)
        self.players_tree.column("num", width=40)
        self.players_tree.column("status", width=100)
        self.players_tree.pack(fill=BOTH, expand=YES, pady=(0, 10))

        btn_row = tb.Frame(list_f)
        btn_row.pack(fill=X)
        tb.Button(btn_row, text="🔢 Смени номер", bootstyle="info-outline",
                  command=self._change_number_dialog).pack(side=LEFT, padx=(0, 5))
        tb.Button(btn_row, text="🗑 Изтрий играч", bootstyle="danger-outline",
                  command=self._delete_player).pack(side=LEFT)

        self._load_club_combos()

    def _load_club_combos(self):
        clubs = list_clubs()
        names = [c["name"] for c in clubs]
        self.player_club_combo.configure(values=names)
        self.player_filter_combo.configure(values=names)
        if names:
            self.player_filter_combo.set(names[0])
            self.player_club_combo.set(names[0])

    def _add_player(self):
        name = self.player_name_entry.get().strip()
        club = self.player_club_combo.get()
        pos = self.player_pos_combo.get()
        num = self.player_num_entry.get().strip()
        if not name or not club or not pos or not num:
            messagebox.showerror("Грешка", "Попълни всички полета")
            return
        try:
            msg = self.players_service.add(name, club, pos, num)
            messagebox.showinfo("Успех", msg)
            self.player_name_entry.delete(0, END)
            self.player_num_entry.delete(0, END)
            self.player_pos_combo.set("")
            self._refresh_players()
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _refresh_players(self):
        for r in self.players_tree.get_children():
            self.players_tree.delete(r)
        club = self.player_filter_combo.get()
        if not club:
            return
        result = self.players_service.list_by_club(club)
        if result.startswith("Грешка") or result == "Няма играчи за този клуб.":
            return
        for line in result.split("\n"):
            parts = line.split(". ", 1)
            if len(parts) != 2:
                continue
            pid = parts[0]
            rest = parts[1]
            rest2 = rest.rsplit(" ", 3)
            if len(rest2) >= 4:
                name = " ".join(rest2[:-3])
                pos = rest2[-3]
                num = rest2[-2].replace("#", "")
                status = rest2[-1].strip("[]")
                self.players_tree.insert("", END, values=(pid, name, pos, num, status))

    def _selected_player(self):
        sel = self.players_tree.selection()
        if not sel:
            messagebox.showerror("Грешка", "Избери играч от списъка")
            return None
        return self.players_tree.item(sel[0])["values"]

    def _change_number_dialog(self):
        vals = self._selected_player()
        if not vals:
            return
        d = NumberDialog(self.root, vals[1])
        if d.result:
            try:
                msg = self.players_service.change_number(vals[1], d.result)
                self._refresh_players()
                messagebox.showinfo("Резултат", msg)
            except ValueError as e:
                messagebox.showerror("Грешка", str(e))

    def _delete_player(self):
        vals = self._selected_player()
        if not vals:
            return
        if messagebox.askyesno("Потвърди", f"Изтриване на '{vals[1]}'?"):
            try:
                msg = self.players_service.delete(vals[1])
                self._refresh_players()
                messagebox.showinfo("Резултат", msg)
            except ValueError as e:
                messagebox.showerror("Грешка", str(e))

    # ==================== TRANSFERS ====================

    def _build_transfers(self, parent):
        tb.Label(parent, text="🔄  Трансфери", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        # Transfer form
        tf = tb.Frame(parent, bootstyle="secondary", padding=12)
        tf.pack(fill=X, pady=(0, 10))
        tb.Label(tf, text="Осъществи трансфер", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        row = tb.Frame(tf)
        row.pack(fill=X)
        tb.Label(row, text="Играч:", width=7).pack(side=LEFT)
        self.tr_player_entry = tb.Entry(row, width=20)
        self.tr_player_entry.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="От:", width=4).pack(side=LEFT)
        self.tr_from_combo = tb.Combobox(row, width=18, state="readonly")
        self.tr_from_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="В:", width=3).pack(side=LEFT)
        self.tr_to_combo = tb.Combobox(row, width=18, state="readonly")
        self.tr_to_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="Дата:", width=5).pack(side=LEFT)
        self.tr_date_entry = tb.Entry(row, width=12)
        self.tr_date_entry.insert(0, "2025-06-01")
        self.tr_date_entry.pack(side=LEFT, padx=(0, 10))
        tb.Label(row, text="Сума:", width=5).pack(side=LEFT)
        self.tr_fee_entry = tb.Entry(row, width=10)
        self.tr_fee_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(row, text="🔄 Трансфер", bootstyle="primary", command=self._do_transfer).pack(side=LEFT)

        # Search
        sf = tb.Frame(parent, bootstyle="secondary", padding=12)
        sf.pack(fill=BOTH, expand=YES)
        tb.Label(sf, text="Трансфери на играч", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        srow = tb.Frame(sf)
        srow.pack(fill=X, pady=(0, 8))
        tb.Label(srow, text="Играч:", width=7).pack(side=LEFT)
        self.tr_search_entry = tb.Entry(srow, width=25)
        self.tr_search_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(srow, text="🔍 Търси", bootstyle="info", command=self._search_transfers).pack(side=LEFT)

        self.tr_result_text = tk.Text(sf, height=12, font=("Consolas", 10),
                                       relief="flat", borderwidth=0,
                                       bg="#303030", fg="#e0e0e0")
        self.tr_result_text.pack(fill=BOTH, expand=YES)

        clubs = list_clubs()
        names = [c["name"] for c in clubs]
        self.tr_from_combo.configure(values=names)
        self.tr_to_combo.configure(values=names)
        if len(names) >= 2:
            self.tr_from_combo.set(names[0])
            self.tr_to_combo.set(names[1])

    def _do_transfer(self):
        player = self.tr_player_entry.get().strip()
        from_c = self.tr_from_combo.get()
        to_c = self.tr_to_combo.get()
        date = self.tr_date_entry.get().strip()
        fee = self.tr_fee_entry.get().strip() or None
        if not player or not from_c or not to_c or not date:
            messagebox.showerror("Грешка", "Попълни всички полета")
            return
        try:
            msg = self.transfers_service.transfer_player(player, from_c, to_c, date, fee)
            messagebox.showinfo("Успех", msg)
            self.tr_player_entry.delete(0, END)
            self.tr_fee_entry.delete(0, END)
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _search_transfers(self):
        player = self.tr_search_entry.get().strip()
        if not player:
            messagebox.showerror("Грешка", "Въведи име на играч")
            return
        try:
            result = self.transfers_service.list_transfers_by_player(player)
            self.tr_result_text.delete("1.0", END)
            self.tr_result_text.insert("1.0", result)
        except ValueError as e:
            self.tr_result_text.delete("1.0", END)
            self.tr_result_text.insert("1.0", f"Грешка: {e}")

    # ==================== MATCHES ====================

    def _build_matches(self, parent):
        tb.Label(parent, text="📅  Мачове", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        nb = tb.Notebook(parent, bootstyle="primary")
        nb.pack(fill=BOTH, expand=YES)

        # Tab 1: Result
        result_tab = tb.Frame(nb, padding=15)
        nb.add(result_tab, text="📋 Резултат")

        row = tb.Frame(result_tab)
        row.pack(fill=X, pady=15)
        tb.Label(row, text="Домакин:", width=10).pack(side=LEFT)
        self.match_home_combo = tb.Combobox(row, width=22, state="readonly")
        self.match_home_combo.pack(side=LEFT, padx=(0, 15))
        tb.Label(row, text="Гост:", width=6).pack(side=LEFT)
        self.match_away_combo = tb.Combobox(row, width=22, state="readonly")
        self.match_away_combo.pack(side=LEFT, padx=(0, 15))
        tb.Label(row, text="Голове:", width=8).pack(side=LEFT)
        self.match_hg_entry = tb.Entry(row, width=5, justify=CENTER)
        self.match_hg_entry.pack(side=LEFT, padx=(0, 3))
        tb.Label(row, text=":").pack(side=LEFT, padx=(0, 3))
        self.match_ag_entry = tb.Entry(row, width=5, justify=CENTER)
        self.match_ag_entry.pack(side=LEFT, padx=(0, 15))
        tb.Button(row, text="💾 Запиши", bootstyle="primary", command=self._add_result).pack(side=LEFT)

        # Tab 2: Events
        events_tab = tb.Frame(nb, padding=15)
        nb.add(events_tab, text="⚡ Събития")

        srow = tb.Frame(events_tab)
        srow.pack(fill=X, pady=(0, 15))
        tb.Label(srow, text="Избери мач по ID:").pack(side=LEFT, padx=(0, 8))
        self.match_select_entry = tb.Entry(srow, width=10)
        self.match_select_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(srow, text="✅ Избери", bootstyle="primary",
                  command=self._select_match_ui).pack(side=LEFT, padx=(0, 15))

        self.match_status_badge = tb.Label(srow, text="❌ Няма избран мач",
                                            bootstyle="secondary")
        self.match_status_badge.pack(side=LEFT)

        tb.Button(srow, text="🏁 Приключи", bootstyle="danger",
                  command=self._finish_match).pack(side=LEFT, padx=(15, 0))

        # Goal
        goal_f = tb.Frame(events_tab, bootstyle="secondary", padding=12)
        goal_f.pack(fill=X, pady=(0, 10))
        tb.Label(goal_f, text="⚽ Добави гол", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        grow = tb.Frame(goal_f)
        grow.pack(fill=X)
        tb.Label(grow, text="Играч:", width=8).pack(side=LEFT)
        self.goal_player_combo = tb.Combobox(grow, width=22, state="readonly")
        self.goal_player_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(grow, text="Отбор:", width=6).pack(side=LEFT)
        self.goal_club_combo = tb.Combobox(grow, width=18, state="readonly")
        self.goal_club_combo.pack(side=LEFT, padx=(0, 10))
        self.goal_club_combo.bind("<<ComboboxSelected>>", self._update_goal_players)
        tb.Label(grow, text="Минута:", width=7).pack(side=LEFT)
        self.goal_min_entry = tb.Entry(grow, width=6)
        self.goal_min_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(grow, text="⚽ Гол", bootstyle="success", command=self._add_goal).pack(side=LEFT)

        # Card
        card_f = tb.Frame(events_tab, bootstyle="secondary", padding=12)
        card_f.pack(fill=X, pady=(0, 10))
        tb.Label(card_f, text="🟨 Добави картон", font=("Segoe UI", 10, "bold"), bootstyle="inverse-secondary").pack(anchor=W, pady=(0, 5))

        crow = tb.Frame(card_f)
        crow.pack(fill=X)
        tb.Label(crow, text="Играч:", width=8).pack(side=LEFT)
        self.card_player_combo = tb.Combobox(crow, width=22, state="readonly")
        self.card_player_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(crow, text="Отбор:", width=6).pack(side=LEFT)
        self.card_club_combo = tb.Combobox(crow, width=18, state="readonly")
        self.card_club_combo.pack(side=LEFT, padx=(0, 10))
        self.card_club_combo.bind("<<ComboboxSelected>>", self._update_card_players)
        tb.Label(crow, text="Тип:", width=5).pack(side=LEFT)
        self.card_type_combo = tb.Combobox(crow, values=["Y", "R"], width=5, state="readonly")
        self.card_type_combo.pack(side=LEFT, padx=(0, 10))
        tb.Label(crow, text="Минута:", width=7).pack(side=LEFT)
        self.card_min_entry = tb.Entry(crow, width=6)
        self.card_min_entry.pack(side=LEFT, padx=(0, 10))
        tb.Button(crow, text="🟥 Картон", bootstyle="danger", command=self._add_card).pack(side=LEFT)

        # Events viewer
        self.events_text = tk.Text(events_tab, height=8, font=("Consolas", 10),
                                    relief="flat", borderwidth=0,
                                    bg="#303030", fg="#e0e0e0")
        self.events_text.pack(fill=BOTH, expand=YES, pady=(10, 5))
        tb.Button(events_tab, text="🔄 Покажи събития", bootstyle="info-outline",
                  command=self._show_events).pack(pady=(0, 5))

        # Tab 3: All matches by league
        league_tab = tb.Frame(nb, padding=15)
        nb.add(league_tab, text="📊 Всички мачове")

        lrow = tb.Frame(league_tab)
        lrow.pack(fill=X, pady=(0, 10))
        tb.Label(lrow, text="Лига:", width=6).pack(side=LEFT, padx=(0, 8))
        self.match_league_combo = tb.Combobox(lrow, width=25, state="readonly")
        self.match_league_combo.pack(side=LEFT, padx=(0, 10))
        tb.Button(lrow, text="📥 Зареди", bootstyle="primary",
                  command=self._load_league_matches).pack(side=LEFT)

        cols = ("ID", "Кръг", "Дата", "Домакин", "Гост", "Резултат", "Статус")
        self.match_tree = tb.Treeview(league_tab, columns=cols, show="headings",
                                       height=12, bootstyle="primary")
        for c in cols:
            self.match_tree.heading(c, text=c)
            self.match_tree.column(c, width=90 if c != "ID" else 50)
        self.match_tree.column("Домакин", width=170)
        self.match_tree.column("Гост", width=170)
        self.match_tree.column("Резултат", width=70)
        self.match_tree.column("Статус", width=80)
        self.match_tree.pack(fill=BOTH, expand=YES)

        sb = tb.Scrollbar(league_tab, orient=VERTICAL, command=self.match_tree.yview)
        sb.pack(side=RIGHT, fill=Y)
        self.match_tree.configure(yscrollcommand=sb.set)

        clubs = list_clubs()
        names = [c["name"] for c in clubs]
        self.match_home_combo.configure(values=names)
        self.match_away_combo.configure(values=names)
        self.goal_club_combo.configure(values=names)
        self.card_club_combo.configure(values=names)
        if len(names) >= 2:
            self.match_home_combo.set(names[0])
            self.match_away_combo.set(names[1])

        leagues = fetch_all("SELECT DISTINCT name FROM leagues ORDER BY name")
        league_names = [r["name"] for r in leagues]
        self.match_league_combo.configure(values=league_names)
        if league_names:
            self.match_league_combo.set(league_names[0])

    def _select_match_ui(self):
        try:
            mid = int(self.match_select_entry.get().strip())
            vs = self.matches_service.select_match(mid)
            self.current_match_id = mid
            self.match_status_badge.configure(text=f"✅ {vs}", bootstyle="success")
            clubs = [
                self.matches_service.selected_home_club,
                self.matches_service.selected_away_club,
            ]
            self.goal_club_combo.configure(values=clubs)
            self.card_club_combo.configure(values=clubs)
            if clubs:
                self.goal_club_combo.set(clubs[0])
                self.card_club_combo.set(clubs[0])
                self._update_goal_players()
                self._update_card_players()
            messagebox.showinfo("OK", f"Избран мач {mid}: {vs}")
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _update_goal_players(self, event=None):
        club = self.goal_club_combo.get()
        if club:
            players = list_players_by_club(club)
            names = [p["full_name"] for p in players]
            self.goal_player_combo.configure(values=names)
            if names:
                self.goal_player_combo.set(names[0])
            else:
                self.goal_player_combo.set("")

    def _update_card_players(self, event=None):
        club = self.card_club_combo.get()
        if club:
            players = list_players_by_club(club)
            names = [p["full_name"] for p in players]
            self.card_player_combo.configure(values=names)
            if names:
                self.card_player_combo.set(names[0])
            else:
                self.card_player_combo.set("")

    def _refresh_matches_tree(self):
        league = self.match_league_combo.get()
        if not league:
            return
        self._load_league_matches()

    def _finish_match(self):
        if not self.current_match_id:
            messagebox.showerror("Грешка", "Първо избери мач")
            return
        try:
            msg = self.matches_service.set_match_finished()
            self._refresh_matches_tree()
            messagebox.showinfo("OK", msg)
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _add_result(self):
        home = self.match_home_combo.get()
        away = self.match_away_combo.get()
        try:
            hg = int(self.match_hg_entry.get().strip())
            ag = int(self.match_ag_entry.get().strip())
            msg = self.matches_service.add_result(home, away, hg, ag)
            self._refresh_matches_tree()
            messagebox.showinfo("OK", msg)
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _add_goal(self):
        if not self.current_match_id:
            messagebox.showerror("Грешка", "Първо избери мач")
            return
        try:
            minute = int(self.goal_min_entry.get().strip())
            msg = self.matches_service.add_goal(
                self.goal_player_combo.get(),
                self.goal_club_combo.get(), minute)
            self.goal_player_combo.set("")
            self.goal_min_entry.delete(0, END)
            self._refresh_matches_tree()
            messagebox.showinfo("OK", msg)
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _add_card(self):
        if not self.current_match_id:
            messagebox.showerror("Грешка", "Първо избери мач")
            return
        try:
            minute = int(self.card_min_entry.get().strip())
            msg = self.matches_service.add_card(
                self.card_player_combo.get(),
                self.card_club_combo.get(),
                self.card_type_combo.get(), minute)
            self.card_player_combo.set("")
            self.card_min_entry.delete(0, END)
            self.card_type_combo.set("")
            messagebox.showinfo("OK", msg)
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def _show_events(self):
        if not self.current_match_id:
            messagebox.showerror("Грешка", "Няма избран мач")
            return
        try:
            result = self.matches_service.show_events()
            self.events_text.delete("1.0", END)
            self.events_text.insert("1.0", result)
        except ValueError as e:
            self.events_text.delete("1.0", END)
            self.events_text.insert("1.0", f"Грешка: {e}")

    def _load_league_matches(self):
        league = self.match_league_combo.get()
        if not league:
            messagebox.showerror("Грешка", "Избери лига")
            return
        try:
            matches = self.matches_service.get_league_matches(league)
            for row in self.match_tree.get_children():
                self.match_tree.delete(row)
            for m in matches:
                score = f"{m['home_goals']}:{m['away_goals']}"
                self.match_tree.insert("", END, values=(
                    m["id"],
                    f"Кръг {m['round_no']}",
                    m["match_date"],
                    m["home_club"],
                    m["away_club"],
                    score,
                    "⏳" if m["status"] == "SCHEDULED" else "✅",
                ))
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    # ==================== STANDINGS ====================

    def _build_standings(self, parent):
        tb.Label(parent, text="🏆  Класиране", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        row = tb.Frame(parent)
        row.pack(fill=X, pady=(0, 15))
        tb.Label(row, text="Лига:", width=6).pack(side=LEFT)
        self.std_league_combo = tb.Combobox(row, width=22, state="readonly")
        self.std_league_combo.pack(side=LEFT, padx=(0, 15))
        tb.Label(row, text="Сезон:", width=6).pack(side=LEFT)
        self.std_season_combo = tb.Combobox(row, width=14, state="readonly")
        self.std_season_combo.pack(side=LEFT, padx=(0, 15))
        tb.Button(row, text="🔍 Покажи", bootstyle="primary", command=self._refresh_standings).pack(side=LEFT)

        # Fetch leagues
        from db import fetch_all
        leagues = fetch_all("SELECT DISTINCT name FROM leagues ORDER BY name")
        seasons = fetch_all("SELECT DISTINCT season FROM leagues ORDER BY season DESC")
        lnames = [l["name"] for l in leagues]
        snames = [s["season"] for s in seasons]
        self.std_league_combo.configure(values=lnames)
        self.std_season_combo.configure(values=snames)
        if lnames:
            self.std_league_combo.set(lnames[0])
        if snames:
            self.std_season_combo.set(snames[0])

        cols = ("pos", "team", "mp", "w", "d", "l", "gf", "ga", "gd", "pts")
        self.standings_tree = tb.Treeview(parent, columns=cols, show="headings", height=18,
                                           bootstyle="primary")
        headers = [("#", "pos", 30), ("Отбор", "team", 250), ("MP", "mp", 40),
                   ("W", "w", 35), ("D", "d", 35), ("L", "l", 35),
                   ("GF", "gf", 40), ("GA", "ga", 40), ("GD", "gd", 40), ("PTS", "pts", 50)]
        for txt, col, w in headers:
            self.standings_tree.heading(col, text=txt)
            self.standings_tree.column(col, width=w)

        self.standings_tree.tag_configure("top", foreground="#2ecc71")
        self.standings_tree.tag_configure("mid", foreground="#f1c40f")
        self.standings_tree.tag_configure("bottom", foreground="#e74c3c")

        scroll = tb.Scrollbar(parent, orient=VERTICAL, bootstyle="primary",
                               command=self.standings_tree.yview)
        self.standings_tree.configure(yscrollcommand=scroll.set)
        self.standings_tree.pack(side=LEFT, fill=BOTH, expand=YES)
        scroll.pack(side=RIGHT, fill=Y)

    def _refresh_standings(self):
        for r in self.standings_tree.get_children():
            self.standings_tree.delete(r)
        league = self.std_league_combo.get()
        season = self.std_season_combo.get()
        if not league or not season:
            return
        try:
            result = self.standings_service.show_table(league, season)
            for line in result.split("\n"):
                parts = line.split(". ", 1)
                if len(parts) != 2:
                    continue
                pos = int(parts[0])
                segments = parts[1].split(" | ")
                if len(segments) < 2:
                    continue
                team = segments[0]
                stats = segments[1].split(" ")
                mp = w = d = l = gf = ga = gd = pts = ""
                for s in stats:
                    if s.startswith("MP:"): mp = s.split(":")[1]
                    elif s.startswith("W:"): w = s.split(":")[1]
                    elif s.startswith("D:"): d = s.split(":")[1]
                    elif s.startswith("L:"): l = s.split(":")[1]
                    elif s.startswith("GD:"): gd = s.split(":")[1]
                    elif s.startswith("PTS:"): pts = s.split(":")[1]
                    elif ":" in s and not s.startswith(("MP", "W:", "D:", "L:", "GD:", "PTS:")):
                        parts2 = s.split(":")
                        if len(parts2) == 2:
                            gf, ga = parts2
                tag = "top" if pos <= 4 else "bottom" if pos >= 17 else "mid"
                self.standings_tree.insert("", END, values=(pos, team, mp, w, d, l, gf, ga, gd, pts),
                                            tags=(tag,))
        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    # ==================== PREDICT ====================

    def _build_predict(self, parent):
        tb.Label(parent, text="🤖  AI Прогноза", font=("Segoe UI", 18, "bold"),
                 bootstyle="primary").pack(anchor=W, pady=(0, 15))

        # League/Season selector
        selector = tb.Frame(parent)
        selector.pack(fill=X, pady=(0, 15))
        tb.Label(selector, text="Лига:", width=6).pack(side=LEFT)
        self.pred_league_combo = tb.Combobox(selector, width=22, state="readonly")
        self.pred_league_combo.pack(side=LEFT, padx=(0, 10))
        self.pred_league_combo.bind("<<ComboboxSelected>>", self._pred_load_clubs)
        tb.Label(selector, text="Сезон:", width=6).pack(side=LEFT)
        self.pred_season_combo = tb.Combobox(selector, width=14, state="readonly")
        self.pred_season_combo.pack(side=LEFT)
        self.pred_season_combo.bind("<<ComboboxSelected>>", self._pred_load_clubs)

        from db import fetch_all
        leagues = fetch_all("SELECT DISTINCT name FROM leagues ORDER BY name")
        seasons = fetch_all("SELECT DISTINCT season FROM leagues ORDER BY season DESC")
        self.pred_league_combo.configure(values=[l["name"] for l in leagues])
        self.pred_season_combo.configure(values=[s["season"] for s in seasons])
        if leagues:
            self.pred_league_combo.set(leagues[0]["name"])
        if seasons:
            self.pred_season_combo.set(seasons[0]["season"])

        form = tb.Frame(parent)
        form.pack(pady=20)

        tf = tb.Frame(form)
        tf.pack()

        tb.Label(tf, text="🏠  Домакин", font=("Segoe UI", 12, "bold"),
                 bootstyle="success").grid(row=0, column=0, padx=10)
        tb.Label(tf, text="✈  Гост", font=("Segoe UI", 12, "bold"),
                 bootstyle="danger").grid(row=0, column=1, padx=10)

        self.pred_home_combo = tb.Combobox(tf, width=25, state="readonly", font=("Segoe UI", 11))
        self.pred_home_combo.grid(row=1, column=0, padx=10, pady=5)
        self.pred_away_combo = tb.Combobox(tf, width=25, state="readonly", font=("Segoe UI", 11))
        self.pred_away_combo.grid(row=1, column=1, padx=10, pady=5)

        tb.Button(parent, text="🔮 Прогнозирай", bootstyle="primary",
                  command=self._do_predict, padding=(30, 12)).pack(pady=20)

        self.pred_result_label = tb.Label(parent, text="", font=("Segoe UI", 11),
                                           justify=CENTER)
        self.pred_result_label.pack()

        self.pred_bar_frame = tb.Frame(parent)
        self.pred_bar_frame.pack(pady=15, fill=X, padx=80)

        self._pred_load_clubs()

    def _pred_load_clubs(self, event=None):
        league = self.pred_league_combo.get()
        season = self.pred_season_combo.get()
        if not league or not season:
            return
        from db import fetch_all
        rows = fetch_all("""
            SELECT c.name FROM clubs c
            JOIN league_teams lt ON lt.club_id = c.id
            JOIN leagues l ON l.id = lt.league_id
            WHERE l.name = ? AND l.season = ?
            ORDER BY c.name
        """, (league, season))
        names = [r["name"] for r in rows]
        self.pred_home_combo.configure(values=names)
        self.pred_away_combo.configure(values=names)
        if len(names) >= 2:
            self.pred_home_combo.set(names[0])
            self.pred_away_combo.set(names[1])
        elif names:
            self.pred_home_combo.set(names[0])

    def _do_predict(self):
        home = self.pred_home_combo.get()
        away = self.pred_away_combo.get()
        if not home or not away:
            messagebox.showerror("Грешка", "Избери два отбора")
            return
        if home == away:
            messagebox.showerror("Грешка", "Отборите трябва да са различни")
            return
        try:
            result = self.ai_service.predict(home, away)
            lines = result.split("\n")
            if len(lines) >= 4:
                home_pct = int(lines[1].split(": ")[1].rstrip("%"))
                draw_pct = int(lines[2].split(": ")[1].rstrip("%"))
                away_pct = int(lines[3].split(": ")[1].rstrip("%"))
            else:
                return

            self.pred_result_label.configure(text=result)

            for w in self.pred_bar_frame.winfo_children():
                w.destroy()

            bars_data = [
                (f"🏠 {home}", home_pct, "success"),
                (f"🤝 Равен", draw_pct, "warning"),
                (f"✈ {away}", away_pct, "danger"),
            ]

            for label, pct, bs in bars_data:
                row_f = tb.Frame(self.pred_bar_frame)
                row_f.pack(fill=X, pady=5)

                tb.Label(row_f, text=f"{label}: {pct}%",
                         font=("Segoe UI", 12, "bold")).pack(anchor=W)

                pb = tb.Progressbar(row_f, length=500, mode="determinate",
                                     value=pct, bootstyle=f"{bs}-striped")
                pb.pack(fill=X, pady=2)

        except ValueError as e:
            messagebox.showerror("Грешка", str(e))

    def run(self):
        self._refresh_clubs()
        self._refresh_standings()
        self.root.mainloop()


class RenameDialog:
    def __init__(self, parent, old_name):
        self.result = None
        d = tb.Toplevel(parent)
        d.title("Преименувай клуб")
        d.geometry("380x140")
        d.transient(parent)
        d.grab_set()

        tb.Label(d, text=f"Ново име за '{old_name}':",
                 font=("Segoe UI", 11)).pack(pady=(20, 8))
        self.entry = tb.Entry(d, width=30, font=("Segoe UI", 11))
        self.entry.pack(pady=5)
        self.entry.focus()

        def submit():
            self.result = self.entry.get().strip()
            d.destroy()

        def cancel():
            d.destroy()

        btn_f = tb.Frame(d)
        btn_f.pack(pady=10)
        tb.Button(btn_f, text="✅ OK", bootstyle="primary", command=submit).pack(side=LEFT, padx=5)
        tb.Button(btn_f, text="❌ Отказ", bootstyle="secondary-outline", command=cancel).pack(side=LEFT, padx=5)

        d.bind("<Return>", lambda e: submit())
        d.wait_window()


class NumberDialog:
    def __init__(self, parent, player_name):
        self.result = None
        d = tb.Toplevel(parent)
        d.title("Смени номер")
        d.geometry("320x140")
        d.transient(parent)
        d.grab_set()

        tb.Label(d, text=f"Нов номер за '{player_name}':",
                 font=("Segoe UI", 11)).pack(pady=(20, 8))
        self.entry = tb.Entry(d, width=10, font=("Segoe UI", 11))
        self.entry.pack(pady=5)
        self.entry.focus()

        def submit():
            self.result = self.entry.get().strip()
            d.destroy()

        def cancel():
            d.destroy()

        btn_f = tb.Frame(d)
        btn_f.pack(pady=10)
        tb.Button(btn_f, text="✅ OK", bootstyle="primary", command=submit).pack(side=LEFT, padx=5)
        tb.Button(btn_f, text="❌ Отказ", bootstyle="secondary-outline", command=cancel).pack(side=LEFT, padx=5)

        d.bind("<Return>", lambda e: submit())
        d.wait_window()


if __name__ == "__main__":
    app = FootballUI()
    app.run()
