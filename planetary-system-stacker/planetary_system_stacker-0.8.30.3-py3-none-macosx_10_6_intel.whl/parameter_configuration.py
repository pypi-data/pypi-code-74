# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigurationDialog(object):
    def setupUi(self, ConfigurationDialog):
        ConfigurationDialog.setObjectName("ConfigurationDialog")
        ConfigurationDialog.resize(900, 571)
        font = QtGui.QFont()
        font.setPointSize(10)
        ConfigurationDialog.setFont(font)
        self.GridLayout = QtWidgets.QGridLayout(ConfigurationDialog)
        self.GridLayout.setVerticalSpacing(22)
        self.GridLayout.setObjectName("GridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigurationDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.GridLayout.addWidget(self.buttonBox, 1, 2, 1, 2)
        self.restore_standard_values = QtWidgets.QPushButton(ConfigurationDialog)
        self.restore_standard_values.setObjectName("restore_standard_values")
        self.GridLayout.addWidget(self.restore_standard_values, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(ConfigurationDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_workflow = QtWidgets.QWidget()
        self.tab_workflow.setObjectName("tab_workflow")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_workflow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.gpif_comboBox = QtWidgets.QComboBox(self.tab_workflow)
        self.gpif_comboBox.setObjectName("gpif_comboBox")
        self.gridLayout.addWidget(self.gpif_comboBox, 5, 3, 1, 1)
        self.nfs_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.nfs_checkBox.setObjectName("nfs_checkBox")
        self.gridLayout.addWidget(self.nfs_checkBox, 7, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 11, 2, 1, 1)
        self.ipfn_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.ipfn_checkBox.setObjectName("ipfn_checkBox")
        self.gridLayout.addWidget(self.ipfn_checkBox, 7, 0, 1, 2)
        self.gpwptf_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.gpwptf_checkBox.setChecked(True)
        self.gpwptf_checkBox.setObjectName("gpwptf_checkBox")
        self.gridLayout.addWidget(self.gpwptf_checkBox, 1, 0, 1, 1)
        self.nap_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.nap_checkBox.setObjectName("nap_checkBox")
        self.gridLayout.addWidget(self.nap_checkBox, 10, 2, 1, 2)
        self.gpspwr_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.gpspwr_checkBox.setObjectName("gpspwr_checkBox")
        self.gridLayout.addWidget(self.gpspwr_checkBox, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.spp_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.spp_checkBox.setObjectName("spp_checkBox")
        self.gridLayout.addWidget(self.spp_checkBox, 5, 0, 1, 1)
        self.apbs_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.apbs_checkBox.setObjectName("apbs_checkBox")
        self.gridLayout.addWidget(self.apbs_checkBox, 9, 2, 1, 2)
        self.gppl_spinBox = QtWidgets.QSpinBox(self.tab_workflow)
        self.gppl_spinBox.setMaximum(2)
        self.gppl_spinBox.setProperty("value", 1)
        self.gppl_spinBox.setObjectName("gppl_spinBox")
        self.gridLayout.addWidget(self.gppl_spinBox, 1, 3, 1, 1)
        self.pfs_checkBox = QtWidgets.QCheckBox(self.tab_workflow)
        self.pfs_checkBox.setObjectName("pfs_checkBox")
        self.gridLayout.addWidget(self.pfs_checkBox, 8, 2, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.gppl_label_parameter = QtWidgets.QLabel(self.tab_workflow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gppl_label_parameter.sizePolicy().hasHeightForWidth())
        self.gppl_label_parameter.setSizePolicy(sizePolicy)
        self.gppl_label_parameter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gppl_label_parameter.setObjectName("gppl_label_parameter")
        self.gridLayout.addWidget(self.gppl_label_parameter, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 1)
        self.gpif_label_parameter = QtWidgets.QLabel(self.tab_workflow)
        self.gpif_label_parameter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gpif_label_parameter.setObjectName("gpif_label_parameter")
        self.gridLayout.addWidget(self.gpif_label_parameter, 5, 2, 1, 1)
        self.gpbl_label_parameter = QtWidgets.QLabel(self.tab_workflow)
        self.gpbl_label_parameter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gpbl_label_parameter.setObjectName("gpbl_label_parameter")
        self.gridLayout.addWidget(self.gpbl_label_parameter, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.gpbl_combobox = QtWidgets.QComboBox(self.tab_workflow)
        self.gpbl_combobox.setObjectName("gpbl_combobox")
        self.gridLayout.addWidget(self.gpbl_combobox, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 5)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 3)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 3)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(11, 7)
        self.tabWidget.addTab(self.tab_workflow, "")
        self.tab_frames = QtWidgets.QWidget()
        self.tab_frames.setObjectName("tab_frames")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_frames)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 13, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 3, 0, 1, 1)
        self.efs_checkBox = QtWidgets.QCheckBox(self.tab_frames)
        self.efs_checkBox.setObjectName("efs_checkBox")
        self.gridLayout_2.addWidget(self.efs_checkBox, 14, 0, 1, 1)
        self.afm_comboBox = QtWidgets.QComboBox(self.tab_frames)
        self.afm_comboBox.setCurrentText("")
        self.afm_comboBox.setMaxVisibleItems(2)
        self.afm_comboBox.setObjectName("afm_comboBox")
        self.gridLayout_2.addWidget(self.afm_comboBox, 7, 2, 1, 2)
        self.afa_checkBox = QtWidgets.QCheckBox(self.tab_frames)
        self.afa_checkBox.setChecked(True)
        self.afa_checkBox.setObjectName("afa_checkBox")
        self.gridLayout_2.addWidget(self.afa_checkBox, 8, 0, 1, 1)
        self.afrsf_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.afrsf_label_parameter.setObjectName("afrsf_label_parameter")
        self.gridLayout_2.addWidget(self.afrsf_label_parameter, 9, 0, 1, 1)
        self.fgw_slider_value = QtWidgets.QSlider(self.tab_frames)
        self.fgw_slider_value.setMinimum(1)
        self.fgw_slider_value.setMaximum(6)
        self.fgw_slider_value.setSingleStep(1)
        self.fgw_slider_value.setPageStep(1)
        self.fgw_slider_value.setProperty("value", 4)
        self.fgw_slider_value.setSliderPosition(4)
        self.fgw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.fgw_slider_value.setObjectName("fgw_slider_value")
        self.gridLayout_2.addWidget(self.fgw_slider_value, 4, 2, 1, 2)
        self.afafp_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.afafp_label_parameter.setObjectName("afafp_label_parameter")
        self.gridLayout_2.addWidget(self.afafp_label_parameter, 12, 0, 1, 1)
        self.fgw_label_display = QtWidgets.QLabel(self.tab_frames)
        self.fgw_label_display.setObjectName("fgw_label_display")
        self.gridLayout_2.addWidget(self.fgw_label_display, 4, 5, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 4, 4, 1, 1)
        self.afrsf_label_display = QtWidgets.QLabel(self.tab_frames)
        self.afrsf_label_display.setObjectName("afrsf_label_display")
        self.gridLayout_2.addWidget(self.afrsf_label_display, 9, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 11, 0, 1, 1)
        self.afafp_label_display = QtWidgets.QLabel(self.tab_frames)
        self.afafp_label_display.setObjectName("afafp_label_display")
        self.gridLayout_2.addWidget(self.afafp_label_display, 12, 5, 1, 1)
        self.afsw_label_display = QtWidgets.QLabel(self.tab_frames)
        self.afsw_label_display.setObjectName("afsw_label_display")
        self.gridLayout_2.addWidget(self.afsw_label_display, 10, 5, 1, 1)
        self.fgw_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.fgw_label_parameter.setObjectName("fgw_label_parameter")
        self.gridLayout_2.addWidget(self.fgw_label_parameter, 4, 0, 1, 1)
        self.afsw_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.afsw_label_parameter.setObjectName("afsw_label_parameter")
        self.gridLayout_2.addWidget(self.afsw_label_parameter, 10, 0, 1, 1)
        self.afafp_slider_value = QtWidgets.QSlider(self.tab_frames)
        self.afafp_slider_value.setMinimum(3)
        self.afafp_slider_value.setMaximum(30)
        self.afafp_slider_value.setSingleStep(3)
        self.afafp_slider_value.setPageStep(3)
        self.afafp_slider_value.setProperty("value", 6)
        self.afafp_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afafp_slider_value.setObjectName("afafp_slider_value")
        self.gridLayout_2.addWidget(self.afafp_slider_value, 12, 2, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 4, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 5, 0, 2, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem14, 0, 0, 1, 1)
        self.fdb_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.fdb_label_parameter.setObjectName("fdb_label_parameter")
        self.gridLayout_2.addWidget(self.fdb_label_parameter, 1, 0, 1, 1)
        self.afrsf_slider_value = QtWidgets.QSlider(self.tab_frames)
        self.afrsf_slider_value.setMinimum(5)
        self.afrsf_slider_value.setMaximum(80)
        self.afrsf_slider_value.setSingleStep(5)
        self.afrsf_slider_value.setPageStep(5)
        self.afrsf_slider_value.setProperty("value", 25)
        self.afrsf_slider_value.setSliderPosition(25)
        self.afrsf_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afrsf_slider_value.setObjectName("afrsf_slider_value")
        self.gridLayout_2.addWidget(self.afrsf_slider_value, 9, 2, 1, 2)
        self.afsw_slider_value = QtWidgets.QSlider(self.tab_frames)
        self.afsw_slider_value.setMinimum(5)
        self.afsw_slider_value.setMaximum(150)
        self.afsw_slider_value.setSingleStep(5)
        self.afsw_slider_value.setPageStep(5)
        self.afsw_slider_value.setProperty("value", 20)
        self.afsw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afsw_slider_value.setObjectName("afsw_slider_value")
        self.gridLayout_2.addWidget(self.afsw_slider_value, 10, 2, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(271, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 4, 6, 1, 1)
        self.afm_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.afm_label_parameter.setObjectName("afm_label_parameter")
        self.gridLayout_2.addWidget(self.afm_label_parameter, 7, 0, 1, 1)
        self.fco_checkBox = QtWidgets.QCheckBox(self.tab_frames)
        self.fco_checkBox.setObjectName("fco_checkBox")
        self.gridLayout_2.addWidget(self.fco_checkBox, 14, 2, 1, 4)
        self.fdbm_label_parameter = QtWidgets.QLabel(self.tab_frames)
        self.fdbm_label_parameter.setObjectName("fdbm_label_parameter")
        self.gridLayout_2.addWidget(self.fdbm_label_parameter, 2, 0, 1, 1)
        self.fdb_comboBox = QtWidgets.QComboBox(self.tab_frames)
        self.fdb_comboBox.setObjectName("fdb_comboBox")
        self.gridLayout_2.addWidget(self.fdb_comboBox, 1, 2, 1, 4)
        self.fdbm_comboBox = QtWidgets.QComboBox(self.tab_frames)
        self.fdbm_comboBox.setObjectName("fdbm_comboBox")
        self.gridLayout_2.addWidget(self.fdbm_comboBox, 2, 2, 1, 4)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.gridLayout_2.setColumnStretch(6, 7)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(1, 3)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_2.setRowStretch(3, 3)
        self.gridLayout_2.setRowStretch(4, 3)
        self.gridLayout_2.setRowStretch(6, 3)
        self.gridLayout_2.setRowStretch(7, 3)
        self.gridLayout_2.setRowStretch(8, 3)
        self.gridLayout_2.setRowStretch(9, 3)
        self.gridLayout_2.setRowStretch(10, 3)
        self.gridLayout_2.setRowStretch(11, 3)
        self.gridLayout_2.setRowStretch(12, 3)
        self.tabWidget.addTab(self.tab_frames, "")
        self.tab_alignment = QtWidgets.QWidget()
        self.tab_alignment.setObjectName("tab_alignment")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_alignment)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.apsw_slider_value = QtWidgets.QSlider(self.tab_alignment)
        self.apsw_slider_value.setMinimum(6)
        self.apsw_slider_value.setMaximum(30)
        self.apsw_slider_value.setSingleStep(2)
        self.apsw_slider_value.setPageStep(2)
        self.apsw_slider_value.setProperty("value", 10)
        self.apsw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apsw_slider_value.setObjectName("apsw_slider_value")
        self.gridLayout_3.addWidget(self.apsw_slider_value, 3, 2, 1, 1)
        self.apst_label_parameter = QtWidgets.QLabel(self.tab_alignment)
        self.apst_label_parameter.setObjectName("apst_label_parameter")
        self.gridLayout_3.addWidget(self.apst_label_parameter, 5, 0, 1, 1)
        self.apst_slider_value = QtWidgets.QSlider(self.tab_alignment)
        self.apst_slider_value.setMinimum(1)
        self.apst_slider_value.setMaximum(30)
        self.apst_slider_value.setPageStep(5)
        self.apst_slider_value.setProperty("value", 5)
        self.apst_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apst_slider_value.setObjectName("apst_slider_value")
        self.gridLayout_3.addWidget(self.apst_slider_value, 5, 2, 1, 1)
        self.apsw_label_display = QtWidgets.QLabel(self.tab_alignment)
        self.apsw_label_display.setObjectName("apsw_label_display")
        self.gridLayout_3.addWidget(self.apsw_label_display, 3, 4, 1, 1)
        self.apsw_label_parameter = QtWidgets.QLabel(self.tab_alignment)
        self.apsw_label_parameter.setObjectName("apsw_label_parameter")
        self.gridLayout_3.addWidget(self.apsw_label_parameter, 3, 0, 1, 1)
        self.apst_label_display = QtWidgets.QLabel(self.tab_alignment)
        self.apst_label_display.setObjectName("apst_label_display")
        self.gridLayout_3.addWidget(self.apst_label_display, 5, 4, 1, 1)
        self.aphbw_slider_value = QtWidgets.QSlider(self.tab_alignment)
        self.aphbw_slider_value.setMinimum(20)
        self.aphbw_slider_value.setMaximum(140)
        self.aphbw_slider_value.setSingleStep(4)
        self.aphbw_slider_value.setPageStep(4)
        self.aphbw_slider_value.setProperty("value", 40)
        self.aphbw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.aphbw_slider_value.setObjectName("aphbw_slider_value")
        self.gridLayout_3.addWidget(self.aphbw_slider_value, 1, 2, 1, 1)
        self.aphbw_label_display = QtWidgets.QLabel(self.tab_alignment)
        self.aphbw_label_display.setObjectName("aphbw_label_display")
        self.gridLayout_3.addWidget(self.aphbw_label_display, 1, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem16, 8, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem17, 1, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 1, 3, 1, 1)
        self.apbt_slider_value = QtWidgets.QSlider(self.tab_alignment)
        self.apbt_slider_value.setMinimum(2)
        self.apbt_slider_value.setMaximum(50)
        self.apbt_slider_value.setSingleStep(2)
        self.apbt_slider_value.setPageStep(2)
        self.apbt_slider_value.setProperty("value", 10)
        self.apbt_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apbt_slider_value.setObjectName("apbt_slider_value")
        self.gridLayout_3.addWidget(self.apbt_slider_value, 7, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 5, 1, 1)
        self.apbt_label_parameter = QtWidgets.QLabel(self.tab_alignment)
        self.apbt_label_parameter.setObjectName("apbt_label_parameter")
        self.gridLayout_3.addWidget(self.apbt_label_parameter, 7, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem20, 2, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 4, 0, 1, 1)
        self.apbt_label_display = QtWidgets.QLabel(self.tab_alignment)
        self.apbt_label_display.setObjectName("apbt_label_display")
        self.gridLayout_3.addWidget(self.apbt_label_display, 7, 4, 1, 1)
        self.aphbw_label_parameter = QtWidgets.QLabel(self.tab_alignment)
        self.aphbw_label_parameter.setObjectName("aphbw_label_parameter")
        self.gridLayout_3.addWidget(self.aphbw_label_parameter, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem22, 6, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem23, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 4)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_3.setColumnStretch(5, 7)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 3)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_3.setRowStretch(5, 3)
        self.gridLayout_3.setRowStretch(6, 1)
        self.gridLayout_3.setRowStretch(7, 3)
        self.gridLayout_3.setRowStretch(8, 12)
        self.tabWidget.addTab(self.tab_alignment, "")
        self.tab_stacking = QtWidgets.QWidget()
        self.tab_stacking.setObjectName("tab_stacking")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_stacking)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fnt_label_parameter = QtWidgets.QLabel(self.tab_stacking)
        self.fnt_label_parameter.setObjectName("fnt_label_parameter")
        self.gridLayout_4.addWidget(self.fnt_label_parameter, 4, 0, 1, 1)
        self.fnt_label_display = QtWidgets.QLabel(self.tab_stacking)
        self.fnt_label_display.setObjectName("fnt_label_display")
        self.gridLayout_4.addWidget(self.fnt_label_display, 4, 4, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem24, 2, 0, 1, 1)
        self.fn_checkBox = QtWidgets.QCheckBox(self.tab_stacking)
        self.fn_checkBox.setObjectName("fn_checkBox")
        self.gridLayout_4.addWidget(self.fn_checkBox, 3, 0, 1, 3)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem25, 0, 0, 1, 1)
        self.fnt_slider_value = QtWidgets.QSlider(self.tab_stacking)
        self.fnt_slider_value.setMaximum(40)
        self.fnt_slider_value.setPageStep(2)
        self.fnt_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.fnt_slider_value.setObjectName("fnt_slider_value")
        self.gridLayout_4.addWidget(self.fnt_slider_value, 4, 2, 1, 1)
        self.sfdfs_label_parameter = QtWidgets.QLabel(self.tab_stacking)
        self.sfdfs_label_parameter.setObjectName("sfdfs_label_parameter")
        self.gridLayout_4.addWidget(self.sfdfs_label_parameter, 6, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem26, 5, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem27, 7, 0, 1, 1)
        self.sfdfs_comboBox = QtWidgets.QComboBox(self.tab_stacking)
        self.sfdfs_comboBox.setObjectName("sfdfs_comboBox")
        self.gridLayout_4.addWidget(self.sfdfs_comboBox, 6, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem28, 4, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem29, 4, 3, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem30, 4, 5, 1, 1)
        self.apfp_comboBox = QtWidgets.QComboBox(self.tab_stacking)
        self.apfp_comboBox.setObjectName("apfp_comboBox")
        self.gridLayout_4.addWidget(self.apfp_comboBox, 1, 0, 1, 3)
        self.apfp_spinBox = QtWidgets.QSpinBox(self.tab_stacking)
        self.apfp_spinBox.setMinimum(1)
        self.apfp_spinBox.setObjectName("apfp_spinBox")
        self.gridLayout_4.addWidget(self.apfp_spinBox, 1, 3, 1, 2)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 3)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 2)
        self.gridLayout_4.setColumnStretch(5, 7)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 3)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 3)
        self.gridLayout_4.setRowStretch(4, 3)
        self.gridLayout_4.setRowStretch(5, 1)
        self.gridLayout_4.setRowStretch(6, 3)
        self.gridLayout_4.setRowStretch(7, 7)
        self.tabWidget.addTab(self.tab_stacking, "")
        self.GridLayout.addWidget(self.tabWidget, 0, 0, 1, 4)
        self.GridLayout.setColumnStretch(0, 5)

        self.retranslateUi(ConfigurationDialog)
        self.tabWidget.setCurrentIndex(1)
        self.afm_comboBox.setCurrentIndex(-1)
        self.apsw_slider_value.valueChanged['int'].connect(self.apsw_label_display.setNum)
        self.aphbw_slider_value.valueChanged['int'].connect(self.aphbw_label_display.setNum)
        self.apbt_slider_value.valueChanged['int'].connect(self.apbt_label_display.setNum)
        self.afsw_slider_value.valueChanged['int'].connect(self.afsw_label_display.setNum)
        self.afrsf_slider_value.valueChanged['int'].connect(self.afrsf_label_display.setNum)
        self.afafp_slider_value.valueChanged['int'].connect(self.afafp_label_display.setNum)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDialog)

    def retranslateUi(self, ConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationDialog.setWindowTitle(_translate("ConfigurationDialog", "Parameter Configuration"))
        self.restore_standard_values.setToolTip(_translate("ConfigurationDialog", "Reset parameters to original values. In most cases they should give satisfactory results."))
        self.restore_standard_values.setText(_translate("ConfigurationDialog", "Restore standard values"))
        self.nfs_checkBox.setText(_translate("ConfigurationDialog", "Number of frames to be stacked"))
        self.ipfn_checkBox.setToolTip(_translate("ConfigurationDialog", "The user can choose which parameter values are encoded in the name of the stacking output file name."))
        self.ipfn_checkBox.setText(_translate("ConfigurationDialog", "Include parameters in output file name"))
        self.gpwptf_checkBox.setToolTip(_translate("ConfigurationDialog", "Append a protocol of this program execution to the text file \"PlanetarySystemStacker.log\" in the user\'s home directory."))
        self.gpwptf_checkBox.setText(_translate("ConfigurationDialog", "Write protocol to file"))
        self.nap_checkBox.setText(_translate("ConfigurationDialog", "Number of alignment points"))
        self.gpspwr_checkBox.setToolTip(_translate("ConfigurationDialog", "Check if for each job the corresponding protocol section should be stored along with the stacked image."))
        self.gpspwr_checkBox.setText(_translate("ConfigurationDialog", "Store protocol with results"))
        self.spp_checkBox.setToolTip(_translate("ConfigurationDialog", "Postprocess the stacked image immediately after stacking,\n"
"rather than in a separate job"))
        self.spp_checkBox.setText(_translate("ConfigurationDialog", "Stacking plus postprocessing"))
        self.apbs_checkBox.setText(_translate("ConfigurationDialog", "Alignment point box size (pixels)"))
        self.pfs_checkBox.setText(_translate("ConfigurationDialog", "Percent of frames to be stacked"))
        self.gppl_label_parameter.setToolTip(_translate("ConfigurationDialog", "Level of detail of protocol: 0 for nothing, 1 for major steps only, 2 for detailed info."))
        self.gppl_label_parameter.setText(_translate("ConfigurationDialog", "Protocol detail level"))
        self.gpif_label_parameter.setToolTip(_translate("ConfigurationDialog", "Stacked and postprocessed images can be written either in \"png\", \"tiff\" or \"fits\" format."))
        self.gpif_label_parameter.setText(_translate("ConfigurationDialog", "Write images as"))
        self.gpbl_label_parameter.setToolTip(_translate("ConfigurationDialog", "Level of data buffering, 0 for no buffering, 4 for buffering all frames and intermediate results."))
        self.gpbl_label_parameter.setText(_translate("ConfigurationDialog", "Data buffering level"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_workflow), _translate("ConfigurationDialog", "Workflow Parameters"))
        self.efs_checkBox.setToolTip(_translate("ConfigurationDialog", "Include a dialog where the user can select frames which should not be used in the stacking workflow."))
        self.efs_checkBox.setText(_translate("ConfigurationDialog", "Dialog to exclude frames from stacking"))
        self.afa_checkBox.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Identify frame stabilization patch automatically."))
        self.afa_checkBox.setText(_translate("ConfigurationDialog", "Automatic frame stabilization"))
        self.afrsf_label_parameter.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Size of the stabilization patch relative to the frame size."))
        self.afrsf_label_parameter.setText(_translate("ConfigurationDialog", "Stabilization patch size (% of frame size)"))
        self.afafp_label_parameter.setToolTip(_translate("ConfigurationDialog", "The reference frame for the multipoint alignment is computed as the average of the best frames. This value specifies the number of frames to be used."))
        self.afafp_label_parameter.setText(_translate("ConfigurationDialog", "Percentage of best frames for\n"
"reference frame computation"))
        self.fgw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.afrsf_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.afafp_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.afsw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.fgw_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the presence of noise in the image, shift detection between frames can be misled by spurious local minima.\n"
"Gaussian blur can help finding the global optimum. Try higher values for noisy images."))
        self.fgw_label_parameter.setText(_translate("ConfigurationDialog", "Noise level (add Gaussian blur)"))
        self.afsw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Maximum allowed shift of consecutive frames per coordinate direction in pixels."))
        self.afsw_label_parameter.setText(_translate("ConfigurationDialog", "Stabilization search width (pixels)"))
        self.fdb_label_parameter.setToolTip(_translate("ConfigurationDialog", "Default debayering pattern used if no other pattern is specified for the current job. This pattern is used in creating master frames as well."))
        self.fdb_label_parameter.setText(_translate("ConfigurationDialog", "Debayering default"))
        self.afm_label_parameter.setToolTip(_translate("ConfigurationDialog", "All frames have to be globally aligned with each other before stacking. Two modes are supported: \"Surface\" and \"Planetary\".\n"
"In \"Surface\" mode (moon, sun) a patch with sufficient local contrast is used for image registration.\n"
"In \"Planetary\" mode, the \"centers of gravity\" of all frames are registered with each other."))
        self.afm_label_parameter.setText(_translate("ConfigurationDialog", "Frame stabilization  mode"))
        self.fco_checkBox.setToolTip(_translate("ConfigurationDialog", "The time span from which frames are taken for computing the reference frame is restricted to avoid blur."))
        self.fco_checkBox.setText(_translate("ConfigurationDialog", "Object is changing fast (e.g. Jupiter, Sun)"))
        self.fdbm_label_parameter.setText(_translate("ConfigurationDialog", "Debayering method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_frames), _translate("ConfigurationDialog", "Frame-related Parameters"))
        self.apst_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the automatic construction of alignment point grids, points are discarded if there is too little local structure.\n"
"Higher values result in more points to be discarded. If the value is too low, unreliable alignment points are included."))
        self.apst_label_parameter.setText(_translate("ConfigurationDialog", "Minimum structure"))
        self.apsw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.apsw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Maximum allowed local warp per coordinate direction."))
        self.apsw_label_parameter.setText(_translate("ConfigurationDialog", "Max. alignment search width (pixels)"))
        self.apst_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.aphbw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.apbt_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the automatic construction of alignment point grids, points are discarded if no pixels in the surrounding box are bright enough.\n"
"Higher values result in more points to be discarded. If the value is too low, unreliable alignment points are included."))
        self.apbt_label_parameter.setText(_translate("ConfigurationDialog", "Minimum brightness"))
        self.apbt_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.aphbw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Size of the quadratic box around an alignment point used to measure the local shift.\n"
"Smaller values result in better resolution of locality, but shift detection can fail if local contrast is low."))
        self.aphbw_label_parameter.setText(_translate("ConfigurationDialog", "Alignment box width (pixels)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_alignment), _translate("ConfigurationDialog", "Multipoint Alignment Parameters"))
        self.fnt_label_parameter.setToolTip(_translate("ConfigurationDialog", "Pixels with brightness below this value will not be included in normalization.\n"
"This reduces the effect of background noise in the dark space around the object."))
        self.fnt_label_parameter.setText(_translate("ConfigurationDialog", "Normalization black cut-off"))
        self.fnt_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.fn_checkBox.setToolTip(_translate("ConfigurationDialog", "Normalize the brightness of all frames. This will improve the ranking of frames and alignment patches, and reduce frame blending artifacts in stacking."))
        self.fn_checkBox.setText(_translate("ConfigurationDialog", "Normalize frame brightness"))
        self.sfdfs_label_parameter.setToolTip(_translate("ConfigurationDialog", "During stacking, the number of pixels in each coordinate direction is multiplied with this factor."))
        self.sfdfs_label_parameter.setText(_translate("ConfigurationDialog", "Use drizzling factor in stacking"))
        self.apfp_comboBox.setToolTip(_translate("ConfigurationDialog", "At each alignment point the same number of frames are stacked.\n"
"This value can either be specified explicitly or by the percentage\n"
"of the total number of frames."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stacking), _translate("ConfigurationDialog", "Stacking Parameters"))
