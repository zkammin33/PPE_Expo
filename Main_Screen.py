# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Screen.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1900, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1900, 900))
        Form.setMaximumSize(QSize(1900, 900))
        Form.setAutoFillBackground(False)
        self.actions_frame = QFrame(Form)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setGeometry(QRect(20, 20, 240, 431))
        self.actions_frame.setFrameShape(QFrame.WinPanel)
        self.actions_frame.setFrameShadow(QFrame.Plain)
        self.inventory_button = QPushButton(self.actions_frame)
        self.inventory_button.setObjectName(u"inventory_button")
        self.inventory_button.setGeometry(QRect(25, 160, 191, 111))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.inventory_button.setFont(font)
        self.report_button = QPushButton(self.actions_frame)
        self.report_button.setObjectName(u"report_button")
        self.report_button.setGeometry(QRect(25, 20, 191, 111))
        self.report_button.setFont(font)
        self.genrep_button = QPushButton(self.actions_frame)
        self.genrep_button.setObjectName(u"genrep_button")
        self.genrep_button.setGeometry(QRect(25, 300, 191, 111))
        self.genrep_button.setFont(font)
        self.aux_frame = QFrame(Form)
        self.aux_frame.setObjectName(u"aux_frame")
        self.aux_frame.setGeometry(QRect(20, 630, 240, 241))
        self.aux_frame.setFrameShape(QFrame.Panel)
        self.aux_frame.setFrameShadow(QFrame.Sunken)
        self.aux_frame.setLineWidth(10)
        self.Logout_Button = QPushButton(self.aux_frame)
        self.Logout_Button.setObjectName(u"Logout_Button")
        self.Logout_Button.setGeometry(QRect(25, 180, 191, 35))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.Logout_Button.setFont(font1)
        self.Logout_Button.setAutoDefault(False)
        self.Logout_Button.setFlat(False)
        self.scan_button = QPushButton(self.aux_frame)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(25, 30, 191, 35))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.scan_button.setFont(font2)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setFlat(False)
        self.main_widget = QStackedWidget(Form)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(280, 20, 1581, 851))
        self.main_widget.setFrameShape(QFrame.Box)
        self.main_widget.setFrameShadow(QFrame.Raised)
        self.report_expo_page = QWidget()
        self.report_expo_page.setObjectName(u"report_expo_page")
        self.calendar_widget = QCalendarWidget(self.report_expo_page)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setGeometry(QRect(20, 40, 351, 191))
        self.submit_expo_btn = QPushButton(self.report_expo_page)
        self.submit_expo_btn.setObjectName(u"submit_expo_btn")
        self.submit_expo_btn.setGeometry(QRect(1390, 800, 171, 41))
        self.select_date_label = QLabel(self.report_expo_page)
        self.select_date_label.setObjectName(u"select_date_label")
        self.select_date_label.setGeometry(QRect(20, 10, 161, 16))
        font3 = QFont()
        font3.setPointSize(12)
        self.select_date_label.setFont(font3)
        self.inc_type_gb = QGroupBox(self.report_expo_page)
        self.inc_type_gb.setObjectName(u"inc_type_gb")
        self.inc_type_gb.setGeometry(QRect(20, 340, 271, 81))
        self.inc_type_gb.setFont(font3)
        self.inc_type_gb.setAlignment(Qt.AlignCenter)
        self.inc_type_gb.setFlat(False)
        self.inc_type_gb.setCheckable(False)
        self.inc_type_cmb = QComboBox(self.inc_type_gb)
        self.inc_type_cmb.addItem("")
        self.inc_type_cmb.addItem("")
        self.inc_type_cmb.addItem("")
        self.inc_type_cmb.addItem("")
        self.inc_type_cmb.setObjectName(u"inc_type_cmb")
        self.inc_type_cmb.setGeometry(QRect(20, 30, 231, 31))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.inc_type_cmb.setFont(font4)
        self.inc_num_gb = QGroupBox(self.report_expo_page)
        self.inc_num_gb.setObjectName(u"inc_num_gb")
        self.inc_num_gb.setGeometry(QRect(20, 250, 271, 81))
        self.inc_num_gb.setFont(font3)
        self.inc_num_gb.setAlignment(Qt.AlignCenter)
        self.inc_num_gb.setFlat(False)
        self.inc_num_gb.setCheckable(False)
        self.inc_num_edit = QLineEdit(self.inc_num_gb)
        self.inc_num_edit.setObjectName(u"inc_num_edit")
        self.inc_num_edit.setGeometry(QRect(20, 40, 231, 22))
        self.exposure_type_gb = QGroupBox(self.report_expo_page)
        self.exposure_type_gb.setObjectName(u"exposure_type_gb")
        self.exposure_type_gb.setGeometry(QRect(320, 250, 271, 81))
        self.exposure_type_gb.setFont(font3)
        self.exposure_type_gb.setAlignment(Qt.AlignCenter)
        self.exposure_type_gb.setFlat(False)
        self.exposure_type_gb.setCheckable(False)
        self.expo_type_cmb = QComboBox(self.exposure_type_gb)
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.addItem("")
        self.expo_type_cmb.setObjectName(u"expo_type_cmb")
        self.expo_type_cmb.setGeometry(QRect(20, 30, 231, 31))
        self.expo_type_cmb.setFont(font4)
        self.expo_type_cmb.setCursor(QCursor(Qt.ArrowCursor))
        self.dirty_gear_gb = QGroupBox(self.report_expo_page)
        self.dirty_gear_gb.setObjectName(u"dirty_gear_gb")
        self.dirty_gear_gb.setGeometry(QRect(20, 430, 271, 81))
        self.dirty_gear_gb.setFont(font3)
        self.dirty_gear_gb.setAlignment(Qt.AlignCenter)
        self.dirty_gear_gb.setFlat(False)
        self.dirty_gear_gb.setCheckable(False)
        self.dirty_gear_combo = QComboBox(self.dirty_gear_gb)
        self.dirty_gear_combo.addItem("")
        self.dirty_gear_combo.addItem("")
        self.dirty_gear_combo.addItem("")
        self.dirty_gear_combo.setObjectName(u"dirty_gear_combo")
        self.dirty_gear_combo.setGeometry(QRect(20, 30, 231, 31))
        self.dirty_gear_combo.setFont(font4)
        self.expo_type_widget = QStackedWidget(self.report_expo_page)
        self.expo_type_widget.setObjectName(u"expo_type_widget")
        self.expo_type_widget.setGeometry(QRect(680, 20, 881, 761))
        self.expo_type_widget.setFrameShape(QFrame.Box)
        self.expo_type_widget.setFrameShadow(QFrame.Sunken)
        self.expo_type_widget.setLineWidth(2)
        self.expo_fire_page = QWidget()
        self.expo_fire_page.setObjectName(u"expo_fire_page")
        self.what_burn_gb = QGroupBox(self.expo_fire_page)
        self.what_burn_gb.setObjectName(u"what_burn_gb")
        self.what_burn_gb.setGeometry(QRect(30, 20, 330, 100))
        font5 = QFont()
        font5.setPointSize(16)
        self.what_burn_gb.setFont(font5)
        self.what_burn_gb.setAlignment(Qt.AlignCenter)
        self.what_burn_gb.setFlat(False)
        self.what_burn_gb.setCheckable(False)
        self.what_burn_cmb = QComboBox(self.what_burn_gb)
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.addItem("")
        self.what_burn_cmb.setObjectName(u"what_burn_cmb")
        self.what_burn_cmb.setGeometry(QRect(20, 40, 290, 40))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.what_burn_cmb.setFont(font6)
        self.fire_cond_gb = QGroupBox(self.expo_fire_page)
        self.fire_cond_gb.setObjectName(u"fire_cond_gb")
        self.fire_cond_gb.setGeometry(QRect(30, 440, 330, 100))
        self.fire_cond_gb.setFont(font3)
        self.fire_cond_gb.setAlignment(Qt.AlignCenter)
        self.fire_cond_gb.setFlat(False)
        self.fire_cond_gb.setCheckable(False)
        self.fire_cond_cmb = QComboBox(self.fire_cond_gb)
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.addItem("")
        self.fire_cond_cmb.setObjectName(u"fire_cond_cmb")
        self.fire_cond_cmb.setGeometry(QRect(20, 30, 290, 40))
        self.fire_cond_cmb.setFont(font4)
        self.smoke_inter_gb = QGroupBox(self.expo_fire_page)
        self.smoke_inter_gb.setObjectName(u"smoke_inter_gb")
        self.smoke_inter_gb.setGeometry(QRect(30, 160, 330, 100))
        self.smoke_inter_gb.setFont(font3)
        self.smoke_inter_gb.setAlignment(Qt.AlignCenter)
        self.smoke_inter_gb.setFlat(False)
        self.smoke_inter_gb.setCheckable(False)
        self.smoke_inter_cmb = QComboBox(self.smoke_inter_gb)
        self.smoke_inter_cmb.addItem("")
        self.smoke_inter_cmb.addItem("")
        self.smoke_inter_cmb.addItem("")
        self.smoke_inter_cmb.setObjectName(u"smoke_inter_cmb")
        self.smoke_inter_cmb.setGeometry(QRect(20, 40, 290, 40))
        self.smoke_inter_cmb.setFont(font4)
        self.foam_gb = QGroupBox(self.expo_fire_page)
        self.foam_gb.setObjectName(u"foam_gb")
        self.foam_gb.setGeometry(QRect(30, 300, 330, 100))
        self.foam_gb.setFont(font3)
        self.foam_gb.setAlignment(Qt.AlignCenter)
        self.foam_gb.setFlat(False)
        self.foam_gb.setCheckable(False)
        self.foam_cmb = QComboBox(self.foam_gb)
        self.foam_cmb.addItem("")
        self.foam_cmb.addItem("")
        self.foam_cmb.addItem("")
        self.foam_cmb.setObjectName(u"foam_cmb")
        self.foam_cmb.setGeometry(QRect(20, 30, 290, 40))
        self.foam_cmb.setFont(font4)
        self.foam_cmb.setCursor(QCursor(Qt.ArrowCursor))
        self.foam_cmb.setEditable(False)
        self.expo_type_widget.addWidget(self.expo_fire_page)
        self.expo_ems_page = QWidget()
        self.expo_ems_page.setObjectName(u"expo_ems_page")
        self.ems_expo_type_gb = QGroupBox(self.expo_ems_page)
        self.ems_expo_type_gb.setObjectName(u"ems_expo_type_gb")
        self.ems_expo_type_gb.setGeometry(QRect(90, 40, 271, 81))
        self.ems_expo_type_gb.setFont(font3)
        self.ems_expo_type_gb.setAlignment(Qt.AlignCenter)
        self.ems_expo_type_gb.setFlat(False)
        self.ems_expo_type_gb.setCheckable(False)
        self.bio_radio_btn = QRadioButton(self.ems_expo_type_gb)
        self.bio_radio_btn.setObjectName(u"bio_radio_btn")
        self.bio_radio_btn.setGeometry(QRect(30, 40, 91, 21))
        self.chem_radio_btn = QRadioButton(self.ems_expo_type_gb)
        self.chem_radio_btn.setObjectName(u"chem_radio_btn")
        self.chem_radio_btn.setGeometry(QRect(160, 40, 91, 21))
        self.bio_chem_widget = QStackedWidget(self.expo_ems_page)
        self.bio_chem_widget.setObjectName(u"bio_chem_widget")
        self.bio_chem_widget.setEnabled(True)
        self.bio_chem_widget.setGeometry(QRect(90, 130, 271, 391))
        self.bio_chem_widget.setFrameShape(QFrame.Box)
        self.bio_chem_widget.setFrameShadow(QFrame.Plain)
        self.bio_page = QWidget()
        self.bio_page.setObjectName(u"bio_page")
        self.fluid_chkbx = QCheckBox(self.bio_page)
        self.fluid_chkbx.setObjectName(u"fluid_chkbx")
        self.fluid_chkbx.setGeometry(QRect(10, 10, 161, 41))
        self.fluid_chkbx.setFont(font1)
        self.skin_infect_chkbx = QCheckBox(self.bio_page)
        self.skin_infect_chkbx.setObjectName(u"skin_infect_chkbx")
        self.skin_infect_chkbx.setGeometry(QRect(10, 70, 161, 41))
        self.skin_infect_chkbx.setFont(font1)
        self.bio_airbrn_chkbx = QCheckBox(self.bio_page)
        self.bio_airbrn_chkbx.setObjectName(u"bio_airbrn_chkbx")
        self.bio_airbrn_chkbx.setGeometry(QRect(10, 130, 111, 41))
        self.bio_airbrn_chkbx.setFont(font1)
        self.contagious_chkbx = QCheckBox(self.bio_page)
        self.contagious_chkbx.setObjectName(u"contagious_chkbx")
        self.contagious_chkbx.setGeometry(QRect(10, 180, 251, 61))
        self.contagious_chkbx.setFont(font1)
        self.fld_water_chkbx = QCheckBox(self.bio_page)
        self.fld_water_chkbx.setObjectName(u"fld_water_chkbx")
        self.fld_water_chkbx.setGeometry(QRect(10, 260, 141, 31))
        self.fld_water_chkbx.setFont(font1)
        self.bio_other_chkbx = QCheckBox(self.bio_page)
        self.bio_other_chkbx.setObjectName(u"bio_other_chkbx")
        self.bio_other_chkbx.setGeometry(QRect(10, 320, 81, 31))
        self.bio_other_chkbx.setFont(font1)
        self.bio_other_edit = QLineEdit(self.bio_page)
        self.bio_other_edit.setObjectName(u"bio_other_edit")
        self.bio_other_edit.setEnabled(False)
        self.bio_other_edit.setGeometry(QRect(10, 350, 251, 22))
        self.bio_chem_widget.addWidget(self.bio_page)
        self.chem_page = QWidget()
        self.chem_page.setObjectName(u"chem_page")
        self.chem_airbrn_chkbx = QCheckBox(self.chem_page)
        self.chem_airbrn_chkbx.setObjectName(u"chem_airbrn_chkbx")
        self.chem_airbrn_chkbx.setGeometry(QRect(10, 40, 161, 41))
        self.chem_airbrn_chkbx.setFont(font1)
        self.skin_contact_chkbx = QCheckBox(self.chem_page)
        self.skin_contact_chkbx.setObjectName(u"skin_contact_chkbx")
        self.skin_contact_chkbx.setGeometry(QRect(10, 110, 161, 41))
        self.skin_contact_chkbx.setFont(font1)
        self.tox_water_chkbx = QCheckBox(self.chem_page)
        self.tox_water_chkbx.setObjectName(u"tox_water_chkbx")
        self.tox_water_chkbx.setGeometry(QRect(10, 180, 161, 41))
        self.tox_water_chkbx.setFont(font1)
        self.chem_other_chkbx = QCheckBox(self.chem_page)
        self.chem_other_chkbx.setObjectName(u"chem_other_chkbx")
        self.chem_other_chkbx.setGeometry(QRect(10, 250, 161, 41))
        self.chem_other_chkbx.setFont(font1)
        self.chem_other_edit = QLineEdit(self.chem_page)
        self.chem_other_edit.setObjectName(u"chem_other_edit")
        self.chem_other_edit.setEnabled(False)
        self.chem_other_edit.setGeometry(QRect(10, 310, 251, 22))
        self.bio_chem_widget.addWidget(self.chem_page)
        self.expo_type_blank_page = QWidget()
        self.expo_type_blank_page.setObjectName(u"expo_type_blank_page")
        self.bio_chem_widget.addWidget(self.expo_type_blank_page)
        self.worn_equp_gb = QGroupBox(self.expo_ems_page)
        self.worn_equp_gb.setObjectName(u"worn_equp_gb")
        self.worn_equp_gb.setGeometry(QRect(470, 120, 311, 411))
        self.worn_equp_gb.setFont(font3)
        self.worn_equp_gb.setAlignment(Qt.AlignCenter)
        self.worn_equp_gb.setFlat(False)
        self.worn_equp_gb.setCheckable(False)
        self.face_cover_chkbx = QCheckBox(self.worn_equp_gb)
        self.face_cover_chkbx.setObjectName(u"face_cover_chkbx")
        self.face_cover_chkbx.setGeometry(QRect(10, 30, 181, 41))
        self.face_cover_chkbx.setFont(font2)
        self.face_cover_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.face_cover_chkbx.setIconSize(QSize(16, 16))
        self.face_cover_chkbx.setChecked(False)
        self.face_cover_chkbx.setTristate(False)
        self.eye_prot_chkbx = QCheckBox(self.worn_equp_gb)
        self.eye_prot_chkbx.setObjectName(u"eye_prot_chkbx")
        self.eye_prot_chkbx.setGeometry(QRect(10, 220, 191, 31))
        self.eye_prot_chkbx.setFont(font2)
        self.eye_prot_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.eye_prot_chkbx.setIconSize(QSize(16, 16))
        self.eye_prot_chkbx.setChecked(False)
        self.eye_prot_chkbx.setTristate(False)
        self.resp_prot_chkbx = QCheckBox(self.worn_equp_gb)
        self.resp_prot_chkbx.setObjectName(u"resp_prot_chkbx")
        self.resp_prot_chkbx.setGeometry(QRect(10, 100, 281, 31))
        self.resp_prot_chkbx.setFont(font2)
        self.resp_prot_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.resp_prot_chkbx.setIconSize(QSize(16, 16))
        self.resp_prot_chkbx.setChecked(False)
        self.resp_prot_chkbx.setTristate(False)
        self.mask_chkbx = QCheckBox(self.worn_equp_gb)
        self.mask_chkbx.setObjectName(u"mask_chkbx")
        self.mask_chkbx.setGeometry(QRect(10, 290, 101, 21))
        self.mask_chkbx.setFont(font2)
        self.mask_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.mask_chkbx.setIconSize(QSize(16, 16))
        self.mask_chkbx.setChecked(False)
        self.mask_chkbx.setTristate(False)
        self.ems_gloves_chkbx = QCheckBox(self.worn_equp_gb)
        self.ems_gloves_chkbx.setObjectName(u"ems_gloves_chkbx")
        self.ems_gloves_chkbx.setGeometry(QRect(10, 160, 101, 31))
        self.ems_gloves_chkbx.setFont(font2)
        self.ems_gloves_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.ems_gloves_chkbx.setIconSize(QSize(16, 16))
        self.ems_gloves_chkbx.setChecked(False)
        self.ems_gloves_chkbx.setTristate(False)
        self.fluid_resis_chkbx = QCheckBox(self.worn_equp_gb)
        self.fluid_resis_chkbx.setObjectName(u"fluid_resis_chkbx")
        self.fluid_resis_chkbx.setGeometry(QRect(10, 350, 291, 31))
        self.fluid_resis_chkbx.setFont(font2)
        self.fluid_resis_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.fluid_resis_chkbx.setIconSize(QSize(16, 16))
        self.fluid_resis_chkbx.setChecked(False)
        self.fluid_resis_chkbx.setTristate(False)
        self.expo_type_widget.addWidget(self.expo_ems_page)
        self.expo_haz_page = QWidget()
        self.expo_haz_page.setObjectName(u"expo_haz_page")
        self.situation_sev_gb = QGroupBox(self.expo_haz_page)
        self.situation_sev_gb.setObjectName(u"situation_sev_gb")
        self.situation_sev_gb.setGeometry(QRect(10, 20, 271, 81))
        self.situation_sev_gb.setFont(font3)
        self.situation_sev_gb.setAlignment(Qt.AlignCenter)
        self.situation_sev_gb.setFlat(False)
        self.situation_sev_gb.setCheckable(False)
        self.situation_sev_cmb = QComboBox(self.situation_sev_gb)
        self.situation_sev_cmb.addItem("")
        self.situation_sev_cmb.addItem("")
        self.situation_sev_cmb.addItem("")
        self.situation_sev_cmb.setObjectName(u"situation_sev_cmb")
        self.situation_sev_cmb.setGeometry(QRect(20, 30, 231, 31))
        self.situation_sev_cmb.setFont(font4)
        self.situation_sev_cmb.setCursor(QCursor(Qt.ArrowCursor))
        self.mats_search_gb = QGroupBox(self.expo_haz_page)
        self.mats_search_gb.setObjectName(u"mats_search_gb")
        self.mats_search_gb.setGeometry(QRect(310, 20, 481, 351))
        self.mats_search_gb.setFont(font3)
        self.mats_search_gb.setAlignment(Qt.AlignCenter)
        self.mats_line_edit = QLineEdit(self.mats_search_gb)
        self.mats_line_edit.setObjectName(u"mats_line_edit")
        self.mats_line_edit.setGeometry(QRect(20, 60, 301, 31))
        self.mats_search_btn = QPushButton(self.mats_search_gb)
        self.mats_search_btn.setObjectName(u"mats_search_btn")
        self.mats_search_btn.setGeometry(QRect(330, 60, 131, 31))
        self.mats_lists_widget = QListWidget(self.mats_search_gb)
        self.mats_lists_widget.setObjectName(u"mats_lists_widget")
        self.mats_lists_widget.setGeometry(QRect(20, 100, 441, 231))
        self.mats_lists_widget.setFrameShadow(QFrame.Sunken)
        self.mats_lists_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.mats_lists_widget.setWordWrap(True)
        self.label = QLabel(self.mats_search_gb)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 301, 20))
        self.expo_type_widget.addWidget(self.expo_haz_page)
        self.inner_blank_page = QWidget()
        self.inner_blank_page.setObjectName(u"inner_blank_page")
        self.expo_type_widget.addWidget(self.inner_blank_page)
        self.expo_gear_gb = QGroupBox(self.report_expo_page)
        self.expo_gear_gb.setObjectName(u"expo_gear_gb")
        self.expo_gear_gb.setGeometry(QRect(320, 340, 271, 281))
        self.expo_gear_gb.setFont(font3)
        self.expo_gear_gb.setAlignment(Qt.AlignCenter)
        self.expo_gear_gb.setFlat(False)
        self.expo_gear_gb.setCheckable(False)
        self.helmet_chkbx = QCheckBox(self.expo_gear_gb)
        self.helmet_chkbx.setObjectName(u"helmet_chkbx")
        self.helmet_chkbx.setGeometry(QRect(10, 50, 101, 21))
        self.helmet_chkbx.setFont(font2)
        self.helmet_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.helmet_chkbx.setIconSize(QSize(16, 16))
        self.helmet_chkbx.setChecked(False)
        self.helmet_chkbx.setTristate(False)
        self.hood_chkbx = QCheckBox(self.expo_gear_gb)
        self.hood_chkbx.setObjectName(u"hood_chkbx")
        self.hood_chkbx.setGeometry(QRect(160, 50, 101, 21))
        self.hood_chkbx.setFont(font2)
        self.hood_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.hood_chkbx.setIconSize(QSize(16, 16))
        self.hood_chkbx.setChecked(False)
        self.hood_chkbx.setTristate(False)
        self.coat_chkbx = QCheckBox(self.expo_gear_gb)
        self.coat_chkbx.setObjectName(u"coat_chkbx")
        self.coat_chkbx.setGeometry(QRect(10, 110, 101, 21))
        self.coat_chkbx.setFont(font2)
        self.coat_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.coat_chkbx.setIconSize(QSize(16, 16))
        self.coat_chkbx.setChecked(False)
        self.coat_chkbx.setTristate(False)
        self.pants_chkbx = QCheckBox(self.expo_gear_gb)
        self.pants_chkbx.setObjectName(u"pants_chkbx")
        self.pants_chkbx.setGeometry(QRect(160, 110, 101, 21))
        self.pants_chkbx.setFont(font2)
        self.pants_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.pants_chkbx.setIconSize(QSize(16, 16))
        self.pants_chkbx.setChecked(False)
        self.pants_chkbx.setTristate(False)
        self.boots_chkbx = QCheckBox(self.expo_gear_gb)
        self.boots_chkbx.setObjectName(u"boots_chkbx")
        self.boots_chkbx.setGeometry(QRect(10, 170, 101, 21))
        self.boots_chkbx.setFont(font2)
        self.boots_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.boots_chkbx.setIconSize(QSize(16, 16))
        self.boots_chkbx.setChecked(False)
        self.boots_chkbx.setTristate(False)
        self.fire_gloves_chkbx = QCheckBox(self.expo_gear_gb)
        self.fire_gloves_chkbx.setObjectName(u"fire_gloves_chkbx")
        self.fire_gloves_chkbx.setGeometry(QRect(160, 170, 101, 21))
        self.fire_gloves_chkbx.setFont(font2)
        self.fire_gloves_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.fire_gloves_chkbx.setIconSize(QSize(16, 16))
        self.fire_gloves_chkbx.setChecked(False)
        self.fire_gloves_chkbx.setTristate(False)
        self.scba_chkbx = QCheckBox(self.expo_gear_gb)
        self.scba_chkbx.setObjectName(u"scba_chkbx")
        self.scba_chkbx.setGeometry(QRect(10, 230, 101, 21))
        self.scba_chkbx.setFont(font2)
        self.scba_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.scba_chkbx.setIconSize(QSize(16, 16))
        self.scba_chkbx.setChecked(False)
        self.scba_chkbx.setTristate(False)
        self.other_fire_chkbx = QCheckBox(self.expo_gear_gb)
        self.other_fire_chkbx.setObjectName(u"other_fire_chkbx")
        self.other_fire_chkbx.setGeometry(QRect(160, 230, 101, 21))
        self.other_fire_chkbx.setFont(font2)
        self.other_fire_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.other_fire_chkbx.setIconSize(QSize(16, 16))
        self.other_fire_chkbx.setChecked(False)
        self.other_fire_chkbx.setTristate(False)
        self.main_widget.addWidget(self.report_expo_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.main_widget.addWidget(self.page_2)

        self.retranslateUi(Form)

        self.main_widget.setCurrentIndex(0)
        self.expo_type_widget.setCurrentIndex(1)
        self.bio_chem_widget.setCurrentIndex(2)




        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Main Screen", None))
        self.inventory_button.setText(QCoreApplication.translate("Form", u"Inventory", None))
        self.report_button.setText(QCoreApplication.translate("Form", u"Report\n"
"Exposure", None))
        self.genrep_button.setText(QCoreApplication.translate("Form", u"Generate \n"
"Report", None))
        self.Logout_Button.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.scan_button.setText(QCoreApplication.translate("Form", u"Scan Gear", None))
        self.submit_expo_btn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.select_date_label.setText(QCoreApplication.translate("Form", u"Select Date of Exposure", None))
        self.inc_type_gb.setTitle(QCoreApplication.translate("Form", u"Incident Type", None))
        self.inc_type_cmb.setItemText(0, QCoreApplication.translate("Form", u"Selcet One", None))
        self.inc_type_cmb.setItemText(1, QCoreApplication.translate("Form", u"Incident Response", None))
        self.inc_type_cmb.setItemText(2, QCoreApplication.translate("Form", u"In-Station", None))
        self.inc_type_cmb.setItemText(3, QCoreApplication.translate("Form", u"Training", None))

        self.inc_type_cmb.setCurrentText(QCoreApplication.translate("Form", u"Selcet One", None))
        self.inc_type_cmb.setPlaceholderText("")
        self.inc_num_gb.setTitle(QCoreApplication.translate("Form", u"Incident Number", None))
        self.inc_num_edit.setText("")
        self.exposure_type_gb.setTitle(QCoreApplication.translate("Form", u"Exposure Type", None))
        self.expo_type_cmb.setItemText(0, QCoreApplication.translate("Form", u"Select  One", None))
        self.expo_type_cmb.setItemText(1, QCoreApplication.translate("Form", u"Fire", None))
        self.expo_type_cmb.setItemText(2, QCoreApplication.translate("Form", u"EMS", None))
        self.expo_type_cmb.setItemText(3, QCoreApplication.translate("Form", u"Hazmat", None))
        self.expo_type_cmb.setItemText(4, QCoreApplication.translate("Form", u"Technical Rescue", None))
        self.expo_type_cmb.setItemText(5, QCoreApplication.translate("Form", u"Other", None))

        self.expo_type_cmb.setPlaceholderText("")
        self.dirty_gear_gb.setTitle(QCoreApplication.translate("Form", u"Did your gear/PPE get dirty?", None))
        self.dirty_gear_combo.setItemText(0, QCoreApplication.translate("Form", u"Select One", None))
        self.dirty_gear_combo.setItemText(1, QCoreApplication.translate("Form", u"Yes", None))
        self.dirty_gear_combo.setItemText(2, QCoreApplication.translate("Form", u"No", None))

        self.dirty_gear_combo.setCurrentText(QCoreApplication.translate("Form", u"Select One", None))
        self.dirty_gear_combo.setPlaceholderText("")
        self.what_burn_gb.setTitle(QCoreApplication.translate("Form", u"What was burning?", None))
        self.what_burn_cmb.setItemText(0, "")
        self.what_burn_cmb.setItemText(1, QCoreApplication.translate("Form", u"Residental Building", None))
        self.what_burn_cmb.setItemText(2, QCoreApplication.translate("Form", u"Commercial Building", None))
        self.what_burn_cmb.setItemText(3, QCoreApplication.translate("Form", u"Contents", None))
        self.what_burn_cmb.setItemText(4, QCoreApplication.translate("Form", u"Vehicle", None))
        self.what_burn_cmb.setItemText(5, QCoreApplication.translate("Form", u"Trash", None))
        self.what_burn_cmb.setItemText(6, QCoreApplication.translate("Form", u"Wildland", None))
        self.what_burn_cmb.setItemText(7, QCoreApplication.translate("Form", u"Other", None))

        self.what_burn_cmb.setCurrentText("")
        self.what_burn_cmb.setPlaceholderText("")
        self.fire_cond_gb.setTitle(QCoreApplication.translate("Form", u"Fire Condition", None))
        self.fire_cond_cmb.setItemText(0, "")
        self.fire_cond_cmb.setItemText(1, QCoreApplication.translate("Form", u"No Smoke or Fire Showing", None))
        self.fire_cond_cmb.setItemText(2, QCoreApplication.translate("Form", u"Smoke Showing", None))
        self.fire_cond_cmb.setItemText(3, QCoreApplication.translate("Form", u"Fire Showing", None))
        self.fire_cond_cmb.setItemText(4, QCoreApplication.translate("Form", u"Full Structure", None))
        self.fire_cond_cmb.setItemText(5, QCoreApplication.translate("Form", u"Fire Spread Origin Structure", None))

        self.fire_cond_cmb.setCurrentText("")
        self.fire_cond_cmb.setPlaceholderText("")
        self.smoke_inter_gb.setTitle(QCoreApplication.translate("Form", u"Smoke Interaction", None))
        self.smoke_inter_cmb.setItemText(0, "")
        self.smoke_inter_cmb.setItemText(1, QCoreApplication.translate("Form", u"Yes", None))
        self.smoke_inter_cmb.setItemText(2, QCoreApplication.translate("Form", u"No", None))

        self.smoke_inter_cmb.setCurrentText("")
        self.smoke_inter_cmb.setPlaceholderText("")
        self.foam_gb.setTitle(QCoreApplication.translate("Form", u"Foam Used?", None))
        self.foam_cmb.setItemText(0, "")
        self.foam_cmb.setItemText(1, QCoreApplication.translate("Form", u"Yes", None))
        self.foam_cmb.setItemText(2, QCoreApplication.translate("Form", u"No", None))

        self.foam_cmb.setPlaceholderText("")
        self.ems_expo_type_gb.setTitle(QCoreApplication.translate("Form", u"Exposure Type", None))
        self.bio_radio_btn.setText(QCoreApplication.translate("Form", u"Biological", None))
        self.chem_radio_btn.setText(QCoreApplication.translate("Form", u"Chemical", None))
        self.fluid_chkbx.setText(QCoreApplication.translate("Form", u"Fluid Contact", None))
        self.skin_infect_chkbx.setText(QCoreApplication.translate("Form", u"Skin Infection", None))
        self.bio_airbrn_chkbx.setText(QCoreApplication.translate("Form", u"Airborne", None))
        self.contagious_chkbx.setText(QCoreApplication.translate("Form", u"Contagious Emergency\n"
"COVID 19", None))
        self.fld_water_chkbx.setText(QCoreApplication.translate("Form", u"Flood Water", None))
        self.bio_other_chkbx.setText(QCoreApplication.translate("Form", u"Other", None))
        self.chem_airbrn_chkbx.setText(QCoreApplication.translate("Form", u"Airborne", None))
        self.skin_contact_chkbx.setText(QCoreApplication.translate("Form", u"Skin Contact", None))
        self.tox_water_chkbx.setText(QCoreApplication.translate("Form", u"Toxic Water", None))
        self.chem_other_chkbx.setText(QCoreApplication.translate("Form", u"Other", None))
        self.worn_equp_gb.setTitle(QCoreApplication.translate("Form", u"Worn Equipiment", None))
        self.face_cover_chkbx.setText(QCoreApplication.translate("Form", u"Face Covering", None))
        self.eye_prot_chkbx.setText(QCoreApplication.translate("Form", u"Eye Protection", None))
        self.resp_prot_chkbx.setText(QCoreApplication.translate("Form", u"Respiratory Protection", None))
        self.mask_chkbx.setText(QCoreApplication.translate("Form", u"Mask", None))
        self.ems_gloves_chkbx.setText(QCoreApplication.translate("Form", u"Gloves", None))
        self.fluid_resis_chkbx.setText(QCoreApplication.translate("Form", u"Fluid Resistant Clothing", None))
        self.situation_sev_gb.setTitle(QCoreApplication.translate("Form", u"Situation Severity", None))
        self.situation_sev_cmb.setItemText(0, "")
        self.situation_sev_cmb.setItemText(1, QCoreApplication.translate("Form", u"Small Spill (> 55 gallons)", None))
        self.situation_sev_cmb.setItemText(2, QCoreApplication.translate("Form", u"Large Spill (< 55 gallons)", None))

        self.situation_sev_cmb.setPlaceholderText("")
        self.mats_search_gb.setTitle(QCoreApplication.translate("Form", u"Materials Search", None))
        self.mats_search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enter the materials name or UN ID number", None))
        self.expo_gear_gb.setTitle(QCoreApplication.translate("Form", u"Exposed Gear", None))
        self.helmet_chkbx.setText(QCoreApplication.translate("Form", u"Helmet", None))
        self.hood_chkbx.setText(QCoreApplication.translate("Form", u"Hood", None))
        self.coat_chkbx.setText(QCoreApplication.translate("Form", u"Coat", None))
        self.pants_chkbx.setText(QCoreApplication.translate("Form", u"Pants", None))
        self.boots_chkbx.setText(QCoreApplication.translate("Form", u"Boots", None))
        self.fire_gloves_chkbx.setText(QCoreApplication.translate("Form", u"Gloves", None))
        self.scba_chkbx.setText(QCoreApplication.translate("Form", u"SCBA", None))
        self.other_fire_chkbx.setText(QCoreApplication.translate("Form", u"Other", None))
    # retranslateUi

