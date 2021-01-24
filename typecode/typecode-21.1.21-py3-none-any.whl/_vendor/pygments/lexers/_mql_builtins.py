# -*- coding: utf-8 -*-
"""
    pygments.lexers._mql_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Builtins for the MqlLexer.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
types = (
    'AccountBalance',
    'AccountCompany',
    'AccountCredit',
    'AccountCurrency',
    'AccountEquity',
    'AccountFreeMarginCheck',
    'AccountFreeMarginMode',
    'AccountFreeMargin',
    'AccountInfoDouble',
    'AccountInfoInteger',
    'AccountInfoString',
    'AccountLeverage',
    'AccountMargin',
    'AccountName',
    'AccountNumber',
    'AccountProfit',
    'AccountServer',
    'AccountStopoutLevel',
    'AccountStopoutMode',
    'Alert',
    'ArrayBsearch',
    'ArrayCompare',
    'ArrayCopyRates',
    'ArrayCopySeries',
    'ArrayCopy',
    'ArrayDimension',
    'ArrayFill',
    'ArrayFree',
    'ArrayGetAsSeries',
    'ArrayInitialize',
    'ArrayIsDynamic',
    'ArrayIsSeries',
    'ArrayMaximum',
    'ArrayMinimum',
    'ArrayRange',
    'ArrayResize',
    'ArraySetAsSeries',
    'ArraySize',
    'ArraySort',
    'CharArrayToString',
    'CharToString',
    'CharToStr',
    'CheckPointer',
    'ColorToARGB',
    'ColorToString',
    'Comment',
    'CopyClose',
    'CopyHigh',
    'CopyLow',
    'CopyOpen',
    'CopyRates',
    'CopyRealVolume',
    'CopySpread',
    'CopyTickVolume',
    'CopyTime',
    'DayOfWeek',
    'DayOfYear',
    'Day',
    'DebugBreak',
    'Digits',
    'DoubleToString',
    'DoubleToStr',
    'EnumToString',
    'EventChartCustom',
    'EventKillTimer',
    'EventSetMillisecondTimer',
    'EventSetTimer',
    'ExpertRemove',
    'FileClose',
    'FileCopy',
    'FileDelete',
    'FileFindClose',
    'FileFindFirst',
    'FileFindNext',
    'FileFlush',
    'FileGetInteger',
    'FileIsEnding',
    'FileIsExist',
    'FileIsLineEnding',
    'FileMove',
    'FileOpenHistory',
    'FileOpen',
    'FileReadArray',
    'FileReadBool',
    'FileReadDatetime',
    'FileReadDouble',
    'FileReadFloat',
    'FileReadInteger',
    'FileReadLong',
    'FileReadNumber',
    'FileReadString',
    'FileReadStruct',
    'FileSeek',
    'FileSize',
    'FileTell',
    'FileWriteArray',
    'FileWriteDouble',
    'FileWriteFloat',
    'FileWriteInteger',
    'FileWriteLong',
    'FileWriteString',
    'FileWriteStruct',
    'FileWrite',
    'FolderClean',
    'FolderCreate',
    'FolderDelete',
    'GetLastError',
    'GetPointer',
    'GetTickCount',
    'GlobalVariableCheck',
    'GlobalVariableDel',
    'GlobalVariableGet',
    'GlobalVariableName',
    'GlobalVariableSetOnCondition',
    'GlobalVariableSet',
    'GlobalVariableTemp',
    'GlobalVariableTime',
    'GlobalVariablesDeleteAll',
    'GlobalVariablesFlush',
    'GlobalVariablesTotal',
    'HideTestIndicators',
    'Hour',
    'IndicatorBuffers',
    'IndicatorCounted',
    'IndicatorDigits',
    'IndicatorSetDouble',
    'IndicatorSetInteger',
    'IndicatorSetString',
    'IndicatorShortName',
    'IntegerToString',
    'IsConnected',
    'IsDemo',
    'IsDllsAllowed',
    'IsExpertEnabled',
    'IsLibrariesAllowed',
    'IsOptimization',
    'IsStopped',
    'IsTesting',
    'IsTradeAllowed',
    'IsTradeContextBusy',
    'IsVisualMode',
    'MQLInfoInteger',
    'MQLInfoString',
    'MarketInfo',
    'MathAbs',
    'MathArccos',
    'MathArcsin',
    'MathArctan',
    'MathCeil',
    'MathCos',
    'MathExp',
    'MathFloor',
    'MathIsValidNumber',
    'MathLog',
    'MathMax',
    'MathMin',
    'MathMod',
    'MathPow',
    'MathRand',
    'MathRound',
    'MathSin',
    'MathSqrt',
    'MathSrand',
    'MathTan',
    'MessageBox',
    'Minute',
    'Month',
    'NormalizeDouble',
    'ObjectCreate',
    'ObjectDelete',
    'ObjectDescription',
    'ObjectFind',
    'ObjectGetDouble',
    'ObjectGetFiboDescription',
    'ObjectGetInteger',
    'ObjectGetShiftByValue',
    'ObjectGetString',
    'ObjectGetTimeByValue',
    'ObjectGetValueByShift',
    'ObjectGetValueByTime',
    'ObjectGet',
    'ObjectMove',
    'ObjectName',
    'ObjectSetDouble',
    'ObjectSetFiboDescription',
    'ObjectSetInteger',
    'ObjectSetString',
    'ObjectSetText',
    'ObjectSet',
    'ObjectType',
    'ObjectsDeleteAll',
    'ObjectsTotal',
    'OrderCloseBy',
    'OrderClosePrice',
    'OrderCloseTime',
    'OrderClose',
    'OrderComment',
    'OrderCommission',
    'OrderDelete',
    'OrderExpiration',
    'OrderLots',
    'OrderMagicNumber',
    'OrderModify',
    'OrderOpenPrice',
    'OrderOpenTime',
    'OrderPrint',
    'OrderProfit',
    'OrderSelect',
    'OrderSend',
    'OrderStopLoss',
    'OrderSwap',
    'OrderSymbol',
    'OrderTakeProfit',
    'OrderTicket',
    'OrderType',
    'OrdersHistoryTotal',
    'OrdersTotal',
    'PeriodSeconds',
    'Period',
    'PlaySound',
    'Point',
    'PrintFormat',
    'Print',
    'RefreshRates',
    'ResetLastError',
    'ResourceCreate',
    'ResourceFree',
    'ResourceReadImage',
    'ResourceSave',
    'Seconds',
    'SendFTP',
    'SendMail',
    'SendNotification',
    'SeriesInfoInteger',
    'SetIndexArrow',
    'SetIndexBuffer',
    'SetIndexDrawBegin',
    'SetIndexEmptyValue',
    'SetIndexLabel',
    'SetIndexShift',
    'SetIndexStyle',
    'SetLevelStyle',
    'SetLevelValue',
    'ShortArrayToString',
    'ShortToString',
    'Sleep',
    'StrToDouble',
    'StrToInteger',
    'StrToTime',
    'StringAdd',
    'StringBufferLen',
    'StringCompare',
    'StringConcatenate',
    'StringFill',
    'StringFind',
    'StringFormat',
    'StringGetCharacter',
    'StringGetChar',
    'StringInit',
    'StringLen',
    'StringReplace',
    'StringSetCharacter',
    'StringSetChar',
    'StringSplit',
    'StringSubstr',
    'StringToCharArray',
    'StringToColor',
    'StringToDouble',
    'StringToInteger',
    'StringToLower',
    'StringToShortArray',
    'StringToTime',
    'StringToUpper',
    'StringTrimLeft',
    'StringTrimRight',
    'StructToTime',
    'SymbolInfoDouble',
    'SymbolInfoInteger',
    'SymbolInfoSessionQuote',
    'SymbolInfoSessionTrade',
    'SymbolInfoString',
    'SymbolInfoTick',
    'SymbolIsSynchronized',
    'SymbolName',
    'SymbolSelect',
    'SymbolsTotal',
    'Symbol',
    'TerminalClose',
    'TerminalCompany',
    'TerminalName',
    'TerminalPath',
    'TesterStatistics',
    'TextGetSize',
    'TextOut',
    'TextSetFont',
    'TimeCurrent',
    'TimeDayOfWeek',
    'TimeDayOfYear',
    'TimeDaylightSavings',
    'TimeDay',
    'TimeGMTOffset',
    'TimeGMT',
    'TimeHour',
    'TimeLocal',
    'TimeMinute',
    'TimeMonth',
    'TimeSeconds',
    'TimeToString',
    'TimeToStruct',
    'TimeToStr',
    'TimeTradeServer',
    'TimeYear',
    'UninitializeReason',
    'WindowBarsPerChart',
    'WindowExpertName',
    'WindowFind',
    'WindowFirstVisibleBar',
    'WindowHandle',
    'WindowIsVisible',
    'WindowOnDropped',
    'WindowPriceMax',
    'WindowPriceMin',
    'WindowPriceOnDropped',
    'WindowRedraw',
    'WindowScreenShot',
    'WindowTimeOnDropped',
    'WindowXOnDropped',
    'WindowYOnDropped',
    'WindowsTotal',
    'Year',
    'ZeroMemory',
    'iAC',
    'iADX',
    'iAD',
    'iAO',
    'iATR',
    'iAlligator',
    'iBWMFI',
    'iBandsOnArray',
    'iBands',
    'iBarShift',
    'iBars',
    'iBearsPower',
    'iBullsPower',
    'iCCIOnArray',
    'iCCI',
    'iClose',
    'iCustom',
    'iDeMarker',
    'iEnvelopesOnArray',
    'iEnvelopes',
    'iForce',
    'iFractals',
    'iGator',
    'iHighest',
    'iHigh',
    'iIchimoku',
    'iLowest',
    'iLow',
    'iMACD',
    'iMAOnArray',
    'iMA',
    'iMFI',
    'iMomentumOnArray',
    'iMomentum',
    'iOBV',
    'iOpen',
    'iOsMA',
    'iRSIOnArray',
    'iRSI',
    'iRVI',
    'iSAR',
    'iStdDevOnArray',
    'iStdDev',
    'iStochastic',
    'iTime',
    'iVolume',
    'iWPR',
)

constants = (
    'ACCOUNT_BALANCE',
    'ACCOUNT_COMPANY',
    'ACCOUNT_CREDIT',
    'ACCOUNT_CURRENCY',
    'ACCOUNT_EQUITY',
    'ACCOUNT_FREEMARGIN',
    'ACCOUNT_LEVERAGE',
    'ACCOUNT_LIMIT_ORDERS',
    'ACCOUNT_LOGIN',
    'ACCOUNT_MARGIN',
    'ACCOUNT_MARGIN_LEVEL',
    'ACCOUNT_MARGIN_SO_CALL',
    'ACCOUNT_MARGIN_SO_MODE',
    'ACCOUNT_MARGIN_SO_SO',
    'ACCOUNT_NAME',
    'ACCOUNT_PROFIT',
    'ACCOUNT_SERVER',
    'ACCOUNT_STOPOUT_MODE_MONEY',
    'ACCOUNT_STOPOUT_MODE_PERCENT',
    'ACCOUNT_TRADE_ALLOWED',
    'ACCOUNT_TRADE_EXPERT',
    'ACCOUNT_TRADE_MODE',
    'ACCOUNT_TRADE_MODE_CONTEST',
    'ACCOUNT_TRADE_MODE_DEMO',
    'ACCOUNT_TRADE_MODE_REAL',
    'ALIGN_CENTER',
    'ALIGN_LEFT',
    'ALIGN_RIGHT',
    'ANCHOR_BOTTOM',
    'ANCHOR_CENTER',
    'ANCHOR_LEFT',
    'ANCHOR_LEFT_LOWER',
    'ANCHOR_LEFT_UPPER',
    'ANCHOR_LOWER',
    'ANCHOR_RIGHT',
    'ANCHOR_RIGHT_LOWER',
    'ANCHOR_RIGHT_UPPER',
    'ANCHOR_TOP',
    'ANCHOR_UPPER',
    'BORDER_FLAT',
    'BORDER_RAISED',
    'BORDER_SUNKEN',
    'CHARTEVENT_CHART_CHANGE',
    'CHARTEVENT_CLICK',
    'CHARTEVENT_CUSTOM',
    'CHARTEVENT_CUSTOM_LAST',
    'CHARTEVENT_KEYDOWN',
    'CHARTEVENT_MOUSE_MOVE',
    'CHARTEVENT_OBJECT_CHANGE',
    'CHARTEVENT_OBJECT_CLICK',
    'CHARTEVENT_OBJECT_CREATE',
    'CHARTEVENT_OBJECT_DELETE',
    'CHARTEVENT_OBJECT_DRAG',
    'CHARTEVENT_OBJECT_ENDEDIT',
    'CHARTS_MAX',
    'CHART_AUTOSCROLL',
    'CHART_BARS',
    'CHART_BEGIN',
    'CHART_BRING_TO_TOP',
    'CHART_CANDLES',
    'CHART_COLOR_ASK',
    'CHART_COLOR_BACKGROUND',
    'CHART_COLOR_BID',
    'CHART_COLOR_CANDLE_BEAR',
    'CHART_COLOR_CANDLE_BULL',
    'CHART_COLOR_CHART_DOWN',
    'CHART_COLOR_CHART_LINE',
    'CHART_COLOR_CHART_UP',
    'CHART_COLOR_FOREGROUND',
    'CHART_COLOR_GRID',
    'CHART_COLOR_LAST',
    'CHART_COLOR_STOP_LEVEL',
    'CHART_COLOR_VOLUME',
    'CHART_COMMENT',
    'CHART_CURRENT_POS',
    'CHART_DRAG_TRADE_LEVELS',
    'CHART_END',
    'CHART_EVENT_MOUSE_MOVE',
    'CHART_EVENT_OBJECT_CREATE',
    'CHART_EVENT_OBJECT_DELETE',
    'CHART_FIRST_VISIBLE_BAR',
    'CHART_FIXED_MAX',
    'CHART_FIXED_MIN',
    'CHART_FIXED_POSITION',
    'CHART_FOREGROUND',
    'CHART_HEIGHT_IN_PIXELS',
    'CHART_IS_OBJECT',
    'CHART_LINE',
    'CHART_MODE',
    'CHART_MOUSE_SCROLL',
    'CHART_POINTS_PER_BAR',
    'CHART_PRICE_MAX',
    'CHART_PRICE_MIN',
    'CHART_SCALEFIX',
    'CHART_SCALEFIX_11',
    'CHART_SCALE',
    'CHART_SCALE_PT_PER_BAR',
    'CHART_SHIFT',
    'CHART_SHIFT_SIZE',
    'CHART_SHOW_ASK_LINE',
    'CHART_SHOW_BID_LINE',
    'CHART_SHOW_DATE_SCALE',
    'CHART_SHOW_GRID',
    'CHART_SHOW_LAST_LINE',
    'CHART_SHOW_OBJECT_DESCR',
    'CHART_SHOW_OHLC',
    'CHART_SHOW_PERIOD_SEP',
    'CHART_SHOW_PRICE_SCALE',
    'CHART_SHOW_TRADE_LEVELS',
    'CHART_SHOW_VOLUMES',
    'CHART_VISIBLE_BARS',
    'CHART_VOLUME_HIDE',
    'CHART_VOLUME_REAL',
    'CHART_VOLUME_TICK',
    'CHART_WIDTH_IN_BARS',
    'CHART_WIDTH_IN_PIXELS',
    'CHART_WINDOWS_TOTAL',
    'CHART_WINDOW_HANDLE',
    'CHART_WINDOW_IS_VISIBLE',
    'CHART_WINDOW_YDISTANCE',
    'CHAR_MAX',
    'CHAR_MIN',
    'CLR_NONE',
    'CORNER_LEFT_LOWER',
    'CORNER_LEFT_UPPER',
    'CORNER_RIGHT_LOWER',
    'CORNER_RIGHT_UPPER',
    'CP_ACP',
    'CP_MACCP',
    'CP_OEMCP',
    'CP_SYMBOL',
    'CP_THREAD_ACP',
    'CP_UTF7',
    'CP_UTF8',
    'DBL_DIG',
    'DBL_EPSILON',
    'DBL_MANT_DIG',
    'DBL_MAX',
    'DBL_MAX_10_EXP',
    'DBL_MAX_EXP',
    'DBL_MIN',
    'DBL_MIN_10_EXP',
    'DBL_MIN_EXP',
    'DRAW_ARROW',
    'DRAW_FILLING',
    'DRAW_HISTOGRAM',
    'DRAW_LINE',
    'DRAW_NONE',
    'DRAW_SECTION',
    'DRAW_ZIGZAG',
    'EMPTY',
    'EMPTY_VALUE',
    'ERR_ACCOUNT_DISABLED',
    'ERR_BROKER_BUSY',
    'ERR_COMMON_ERROR',
    'ERR_INVALID_ACCOUNT',
    'ERR_INVALID_PRICE',
    'ERR_INVALID_STOPS',
    'ERR_INVALID_TRADE_PARAMETERS',
    'ERR_INVALID_TRADE_VOLUME',
    'ERR_LONG_POSITIONS_ONLY_ALLOWED',
    'ERR_MALFUNCTIONAL_TRADE',
    'ERR_MARKET_CLOSED',
    'ERR_NOT_ENOUGH_MONEY',
    'ERR_NOT_ENOUGH_RIGHTS',
    'ERR_NO_CONNECTION',
    'ERR_NO_ERROR',
    'ERR_NO_RESULT',
    'ERR_OFF_QUOTES',
    'ERR_OLD_VERSION',
    'ERR_ORDER_LOCKED',
    'ERR_PRICE_CHANGED',
    'ERR_REQUOTE',
    'ERR_SERVER_BUSY',
    'ERR_TOO_FREQUENT_REQUESTS',
    'ERR_TOO_MANY_REQUESTS',
    'ERR_TRADE_CONTEXT_BUSY',
    'ERR_TRADE_DISABLED',
    'ERR_TRADE_EXPIRATION_DENIED',
    'ERR_TRADE_HEDGE_PROHIBITED',
    'ERR_TRADE_MODIFY_DENIED',
    'ERR_TRADE_PROHIBITED_BY_FIFO',
    'ERR_TRADE_TIMEOUT',
    'ERR_TRADE_TOO_MANY_ORDERS',
    'FILE_ACCESS_DATE',
    'FILE_ANSI',
    'FILE_BIN',
    'FILE_COMMON',
    'FILE_CREATE_DATE',
    'FILE_CSV',
    'FILE_END',
    'FILE_EXISTS',
    'FILE_IS_ANSI',
    'FILE_IS_BINARY',
    'FILE_IS_COMMON',
    'FILE_IS_CSV',
    'FILE_IS_READABLE',
    'FILE_IS_TEXT',
    'FILE_IS_WRITABLE',
    'FILE_LINE_END',
    'FILE_MODIFY_DATE',
    'FILE_POSITION',
    'FILE_READ',
    'FILE_REWRITE',
    'FILE_SHARE_READ',
    'FILE_SHARE_WRITE',
    'FILE_SIZE',
    'FILE_TXT',
    'FILE_UNICODE',
    'FILE_WRITE',
    'FLT_DIG',
    'FLT_EPSILON',
    'FLT_MANT_DIG',
    'FLT_MAX',
    'FLT_MAX_10_EXP',
    'FLT_MAX_EXP',
    'FLT_MIN',
    'FLT_MIN_10_EXP',
    'FLT_MIN_EXP',
    'FRIDAY',
    'GANN_DOWN_TREND',
    'GANN_UP_TREND',
    'IDABORT',
    'IDCANCEL',
    'IDCONTINUE',
    'IDIGNORE',
    'IDNO',
    'IDOK',
    'IDRETRY',
    'IDTRYAGAIN',
    'IDYES',
    'INDICATOR_CALCULATIONS',
    'INDICATOR_COLOR_INDEX',
    'INDICATOR_DATA',
    'INDICATOR_DIGITS',
    'INDICATOR_HEIGHT',
    'INDICATOR_LEVELCOLOR',
    'INDICATOR_LEVELSTYLE',
    'INDICATOR_LEVELS',
    'INDICATOR_LEVELTEXT',
    'INDICATOR_LEVELVALUE',
    'INDICATOR_LEVELWIDTH',
    'INDICATOR_MAXIMUM',
    'INDICATOR_MINIMUM',
    'INDICATOR_SHORTNAME',
    'INT_MAX',
    'INT_MIN',
    'INVALID_HANDLE',
    'IS_DEBUG_MODE',
    'IS_PROFILE_MODE',
    'LICENSE_DEMO',
    'LICENSE_FREE',
    'LICENSE_FULL',
    'LICENSE_TIME',
    'LONG_MAX',
    'LONG_MIN',
    'MB_ABORTRETRYIGNORE',
    'MB_CANCELTRYCONTINUE',
    'MB_DEFBUTTON1',
    'MB_DEFBUTTON2',
    'MB_DEFBUTTON3',
    'MB_DEFBUTTON4',
    'MB_ICONASTERISK',
    'MB_ICONERROR',
    'MB_ICONEXCLAMATION',
    'MB_ICONHAND',
    'MB_ICONINFORMATION',
    'MB_ICONQUESTION',
    'MB_ICONSTOP',
    'MB_ICONWARNING',
    'MB_OKCANCEL',
    'MB_OK',
    'MB_RETRYCANCEL',
    'MB_YESNOCANCEL',
    'MB_YESNO',
    'MODE_ASK',
    'MODE_BID',
    'MODE_CHINKOUSPAN',
    'MODE_CLOSE',
    'MODE_DIGITS',
    'MODE_EMA',
    'MODE_EXPIRATION',
    'MODE_FREEZELEVEL',
    'MODE_GATORJAW',
    'MODE_GATORLIPS',
    'MODE_GATORTEETH',
    'MODE_HIGH',
    'MODE_KIJUNSEN',
    'MODE_LOTSIZE',
    'MODE_LOTSTEP',
    'MODE_LOWER',
    'MODE_LOW',
    'MODE_LWMA',
    'MODE_MAIN',
    'MODE_MARGINCALCMODE',
    'MODE_MARGINHEDGED',
    'MODE_MARGININIT',
    'MODE_MARGINMAINTENANCE',
    'MODE_MARGINREQUIRED',
    'MODE_MAXLOT',
    'MODE_MINLOT',
    'MODE_MINUSDI',
    'MODE_OPEN',
    'MODE_PLUSDI',
    'MODE_POINT',
    'MODE_PROFITCALCMODE',
    'MODE_SENKOUSPANA',
    'MODE_SENKOUSPANB',
    'MODE_SIGNAL',
    'MODE_SMA',
    'MODE_SMMA',
    'MODE_SPREAD',
    'MODE_STARTING',
    'MODE_STOPLEVEL',
    'MODE_SWAPLONG',
    'MODE_SWAPSHORT',
    'MODE_SWAPTYPE',
    'MODE_TENKANSEN',
    'MODE_TICKSIZE',
    'MODE_TICKVALUE',
    'MODE_TIME',
    'MODE_TRADEALLOWED',
    'MODE_UPPER',
    'MODE_VOLUME',
    'MONDAY',
    'MQL_DEBUG',
    'MQL_DLLS_ALLOWED',
    'MQL_FRAME_MODE',
    'MQL_LICENSE_TYPE',
    'MQL_OPTIMIZATION',
    'MQL_PROFILER',
    'MQL_PROGRAM_NAME',
    'MQL_PROGRAM_PATH',
    'MQL_PROGRAM_TYPE',
    'MQL_TESTER',
    'MQL_TRADE_ALLOWED',
    'MQL_VISUAL_MODE',
    'M_1_PI',
    'M_2_PI',
    'M_2_SQRTPI',
    'M_E',
    'M_LN2',
    'M_LN10',
    'M_LOG2E',
    'M_LOG10E',
    'M_PI',
    'M_PI_2',
    'M_PI_4',
    'M_SQRT1_2',
    'M_SQRT2',
    'NULL',
    'OBJPROP_ALIGN',
    'OBJPROP_ANCHOR',
    'OBJPROP_ANGLE',
    'OBJPROP_ARROWCODE',
    'OBJPROP_BACK',
    'OBJPROP_BGCOLOR',
    'OBJPROP_BMPFILE',
    'OBJPROP_BORDER_COLOR',
    'OBJPROP_BORDER_TYPE',
    'OBJPROP_CHART_ID',
    'OBJPROP_CHART_SCALE',
    'OBJPROP_COLOR',
    'OBJPROP_CORNER',
    'OBJPROP_CREATETIME',
    'OBJPROP_DATE_SCALE',
    'OBJPROP_DEVIATION',
    'OBJPROP_DRAWLINES',
    'OBJPROP_ELLIPSE',
    'OBJPROP_FIBOLEVELS',
    'OBJPROP_FILL',
    'OBJPROP_FIRSTLEVEL',
    'OBJPROP_FONTSIZE',
    'OBJPROP_FONT',
    'OBJPROP_HIDDEN',
    'OBJPROP_LEVELCOLOR',
    'OBJPROP_LEVELSTYLE',
    'OBJPROP_LEVELS',
    'OBJPROP_LEVELTEXT',
    'OBJPROP_LEVELVALUE',
    'OBJPROP_LEVELWIDTH',
    'OBJPROP_NAME',
    'OBJPROP_PERIOD',
    'OBJPROP_PRICE1',
    'OBJPROP_PRICE2',
    'OBJPROP_PRICE3',
    'OBJPROP_PRICE',
    'OBJPROP_PRICE_SCALE',
    'OBJPROP_RAY',
    'OBJPROP_RAY_RIGHT',
    'OBJPROP_READONLY',
    'OBJPROP_SCALE',
    'OBJPROP_SELECTABLE',
    'OBJPROP_SELECTED',
    'OBJPROP_STATE',
    'OBJPROP_STYLE',
    'OBJPROP_SYMBOL',
    'OBJPROP_TEXT',
    'OBJPROP_TIME1',
    'OBJPROP_TIME2',
    'OBJPROP_TIME3',
    'OBJPROP_TIMEFRAMES',
    'OBJPROP_TIME',
    'OBJPROP_TOOLTIP',
    'OBJPROP_TYPE',
    'OBJPROP_WIDTH',
    'OBJPROP_XDISTANCE',
    'OBJPROP_XOFFSET',
    'OBJPROP_XSIZE',
    'OBJPROP_YDISTANCE',
    'OBJPROP_YOFFSET',
    'OBJPROP_YSIZE',
    'OBJPROP_ZORDER',
    'OBJ_ALL_PERIODS',
    'OBJ_ARROW',
    'OBJ_ARROW_BUY',
    'OBJ_ARROW_CHECK',
    'OBJ_ARROW_DOWN',
    'OBJ_ARROW_LEFT_PRICE',
    'OBJ_ARROW_RIGHT_PRICE',
    'OBJ_ARROW_SELL',
    'OBJ_ARROW_STOP',
    'OBJ_ARROW_THUMB_DOWN',
    'OBJ_ARROW_THUMB_UP',
    'OBJ_ARROW_UP',
    'OBJ_BITMAP',
    'OBJ_BITMAP_LABEL',
    'OBJ_BUTTON',
    'OBJ_CHANNEL',
    'OBJ_CYCLES',
    'OBJ_EDIT',
    'OBJ_ELLIPSE',
    'OBJ_EVENT',
    'OBJ_EXPANSION',
    'OBJ_FIBOARC',
    'OBJ_FIBOCHANNEL',
    'OBJ_FIBOFAN',
    'OBJ_FIBOTIMES',
    'OBJ_FIBO',
    'OBJ_GANNFAN',
    'OBJ_GANNGRID',
    'OBJ_GANNLINE',
    'OBJ_HLINE',
    'OBJ_LABEL',
    'OBJ_NO_PERIODS',
    'OBJ_PERIOD_D1',
    'OBJ_PERIOD_H1',
    'OBJ_PERIOD_H4',
    'OBJ_PERIOD_M1',
    'OBJ_PERIOD_M5',
    'OBJ_PERIOD_M15',
    'OBJ_PERIOD_M30',
    'OBJ_PERIOD_MN1',
    'OBJ_PERIOD_W1',
    'OBJ_PITCHFORK',
    'OBJ_RECTANGLE',
    'OBJ_RECTANGLE_LABEL',
    'OBJ_REGRESSION',
    'OBJ_STDDEVCHANNEL',
    'OBJ_TEXT',
    'OBJ_TRENDBYANGLE',
    'OBJ_TREND',
    'OBJ_TRIANGLE',
    'OBJ_VLINE',
    'OP_BUYLIMIT',
    'OP_BUYSTOP',
    'OP_BUY',
    'OP_SELLLIMIT',
    'OP_SELLSTOP',
    'OP_SELL',
    'PERIOD_CURRENT',
    'PERIOD_D1',
    'PERIOD_H1',
    'PERIOD_H2',
    'PERIOD_H3',
    'PERIOD_H4',
    'PERIOD_H6',
    'PERIOD_H8',
    'PERIOD_H12',
    'PERIOD_M1',
    'PERIOD_M2',
    'PERIOD_M3',
    'PERIOD_M4',
    'PERIOD_M5',
    'PERIOD_M6',
    'PERIOD_M10',
    'PERIOD_M12',
    'PERIOD_M15',
    'PERIOD_M20',
    'PERIOD_M30',
    'PERIOD_MN1',
    'PERIOD_W1',
    'POINTER_AUTOMATIC',
    'POINTER_DYNAMIC',
    'POINTER_INVALID'
    'PRICE_CLOSE',
    'PRICE_HIGH',
    'PRICE_LOW',
    'PRICE_MEDIAN',
    'PRICE_OPEN',
    'PRICE_TYPICAL',
    'PRICE_WEIGHTED',
    'PROGRAM_EXPERT',
    'PROGRAM_INDICATOR',
    'PROGRAM_SCRIPT',
    'REASON_ACCOUNT',
    'REASON_CHARTCHANGE',
    'REASON_CHARTCLOSE',
    'REASON_CLOSE',
    'REASON_INITFAILED',
    'REASON_PARAMETERS',
    'REASON_PROGRAM'
    'REASON_RECOMPILE',
    'REASON_REMOVE',
    'REASON_TEMPLATE',
    'SATURDAY',
    'SEEK_CUR',
    'SEEK_END',
    'SEEK_SET',
    'SERIES_BARS_COUNT',
    'SERIES_FIRSTDATE',
    'SERIES_LASTBAR_DATE',
    'SERIES_SERVER_FIRSTDATE',
    'SERIES_SYNCHRONIZED',
    'SERIES_TERMINAL_FIRSTDATE',
    'SHORT_MAX',
    'SHORT_MIN',
    'STAT_BALANCEDD_PERCENT',
    'STAT_BALANCEMIN',
    'STAT_BALANCE_DDREL_PERCENT',
    'STAT_BALANCE_DD',
    'STAT_BALANCE_DD_RELATIVE',
    'STAT_CONLOSSMAX',
    'STAT_CONLOSSMAX_TRADES',
    'STAT_CONPROFITMAX',
    'STAT_CONPROFITMAX_TRADES',
    'STAT_CUSTOM_ONTESTER',
    'STAT_DEALS',
    'STAT_EQUITYDD_PERCENT',
    'STAT_EQUITYMIN',
    'STAT_EQUITY_DDREL_PERCENT',
    'STAT_EQUITY_DD',
    'STAT_EQUITY_DD_RELATIVE',
    'STAT_EXPECTED_PAYOFF',
    'STAT_GROSS_LOSS',
    'STAT_GROSS_PROFIT',
    'STAT_INITIAL_DEPOSIT',
    'STAT_LONG_TRADES',
    'STAT_LOSSTRADES_AVGCON',
    'STAT_LOSS_TRADES',
    'STAT_MAX_CONLOSSES',
    'STAT_MAX_CONLOSS_TRADES',
    'STAT_MAX_CONPROFIT_TRADES',
    'STAT_MAX_CONWINS',
    'STAT_MAX_LOSSTRADE',
    'STAT_MAX_PROFITTRADE',
    'STAT_MIN_MARGINLEVEL',
    'STAT_PROFITTRADES_AVGCON',
    'STAT_PROFIT',
    'STAT_PROFIT_FACTOR',
    'STAT_PROFIT_LONGTRADES',
    'STAT_PROFIT_SHORTTRADES',
    'STAT_PROFIT_TRADES',
    'STAT_RECOVERY_FACTOR',
    'STAT_SHARPE_RATIO',
    'STAT_SHORT_TRADES',
    'STAT_TRADES',
    'STAT_WITHDRAWAL',
    'STO_CLOSECLOSE',
    'STO_LOWHIGH',
    'STYLE_DASHDOTDOT',
    'STYLE_DASHDOT',
    'STYLE_DASH',
    'STYLE_DOT',
    'STYLE_SOLID',
    'SUNDAY',
    'SYMBOL_ARROWDOWN',
    'SYMBOL_ARROWUP',
    'SYMBOL_CHECKSIGN',
    'SYMBOL_LEFTPRICE',
    'SYMBOL_RIGHTPRICE',
    'SYMBOL_STOPSIGN',
    'SYMBOL_THUMBSDOWN',
    'SYMBOL_THUMBSUP',
    'TERMINAL_BUILD',
    'TERMINAL_CODEPAGE',
    'TERMINAL_COMMONDATA_PATH',
    'TERMINAL_COMPANY',
    'TERMINAL_CONNECTED',
    'TERMINAL_CPU_CORES',
    'TERMINAL_DATA_PATH',
    'TERMINAL_DISK_SPACE',
    'TERMINAL_DLLS_ALLOWED',
    'TERMINAL_EMAIL_ENABLED',
    'TERMINAL_FTP_ENABLED',
    'TERMINAL_LANGUAGE',
    'TERMINAL_MAXBARS',
    'TERMINAL_MEMORY_AVAILABLE',
    'TERMINAL_MEMORY_PHYSICAL',
    'TERMINAL_MEMORY_TOTAL',
    'TERMINAL_MEMORY_USED',
    'TERMINAL_NAME',
    'TERMINAL_OPENCL_SUPPORT',
    'TERMINAL_PATH',
    'TERMINAL_TRADE_ALLOWED',
    'TERMINAL_X64',
    'THURSDAY',
    'TRADE_ACTION_DEAL',
    'TRADE_ACTION_MODIFY',
    'TRADE_ACTION_PENDING',
    'TRADE_ACTION_REMOVE',
    'TRADE_ACTION_SLTP',
    'TUESDAY',
    'UCHAR_MAX',
    'UINT_MAX',
    'ULONG_MAX',
    'USHORT_MAX',
    'VOLUME_REAL',
    'VOLUME_TICK',
    'WEDNESDAY',
    'WHOLE_ARRAY',
    'WRONG_VALUE',
    'clrNONE',
    '__DATETIME__',
    '__DATE__',
    '__FILE__',
    '__FUNCSIG__',
    '__FUNCTION__',
    '__LINE__',
    '__MQL4BUILD__',
    '__MQLBUILD__',
    '__PATH__',
)

colors = (
    'AliceBlue',
    'AntiqueWhite',
    'Aquamarine',
    'Aqua',
    'Beige',
    'Bisque',
    'Black',
    'BlanchedAlmond',
    'BlueViolet',
    'Blue',
    'Brown',
    'BurlyWood',
    'CadetBlue',
    'Chartreuse',
    'Chocolate',
    'Coral',
    'CornflowerBlue',
    'Cornsilk',
    'Crimson',
    'DarkBlue',
    'DarkGoldenrod',
    'DarkGray',
    'DarkGreen',
    'DarkKhaki',
    'DarkOliveGreen',
    'DarkOrange',
    'DarkOrchid',
    'DarkSalmon',
    'DarkSeaGreen',
    'DarkSlateBlue',
    'DarkSlateGray',
    'DarkTurquoise',
    'DarkViolet',
    'DeepPink',
    'DeepSkyBlue',
    'DimGray',
    'DodgerBlue',
    'FireBrick',
    'ForestGreen',
    'Gainsboro',
    'Goldenrod',
    'Gold',
    'Gray',
    'GreenYellow',
    'Green',
    'Honeydew',
    'HotPink',
    'IndianRed',
    'Indigo',
    'Ivory',
    'Khaki',
    'LavenderBlush',
    'Lavender',
    'LawnGreen',
    'LemonChiffon',
    'LightBlue',
    'LightCoral',
    'LightCyan',
    'LightGoldenrod',
    'LightGray',
    'LightGreen',
    'LightPink',
    'LightSalmon',
    'LightSeaGreen',
    'LightSkyBlue',
    'LightSlateGray',
    'LightSteelBlue',
    'LightYellow',
    'LimeGreen',
    'Lime',
    'Linen',
    'Magenta',
    'Maroon',
    'MediumAquamarine',
    'MediumBlue',
    'MediumOrchid',
    'MediumPurple',
    'MediumSeaGreen',
    'MediumSlateBlue',
    'MediumSpringGreen',
    'MediumTurquoise',
    'MediumVioletRed',
    'MidnightBlue',
    'MintCream',
    'MistyRose',
    'Moccasin',
    'NavajoWhite',
    'Navy',
    'OldLace',
    'OliveDrab',
    'Olive',
    'OrangeRed',
    'Orange',
    'Orchid',
    'PaleGoldenrod',
    'PaleGreen',
    'PaleTurquoise',
    'PaleVioletRed',
    'PapayaWhip',
    'PeachPuff',
    'Peru',
    'Pink',
    'Plum',
    'PowderBlue',
    'Purple',
    'Red',
    'RosyBrown',
    'RoyalBlue',
    'SaddleBrown',
    'Salmon',
    'SandyBrown',
    'SeaGreen',
    'Seashell',
    'Sienna',
    'Silver',
    'SkyBlue',
    'SlateBlue',
    'SlateGray',
    'Snow',
    'SpringGreen',
    'SteelBlue',
    'Tan',
    'Teal',
    'Thistle',
    'Tomato',
    'Turquoise',
    'Violet',
    'Wheat',
    'WhiteSmoke',
    'White',
    'YellowGreen',
    'Yellow',
)

keywords = (
    'input', '_Digits', '_Point', '_LastError', '_Period', '_RandomSeed',
    '_StopFlag', '_Symbol', '_UninitReason', 'Ask', 'Bars', 'Bid',
    'Close', 'Digits', 'High', 'Low', 'Open', 'Point', 'Time',
    'Volume',
)
c_types = (
    'void', 'char', 'uchar', 'bool', 'short', 'ushort', 'int', 'uint',
    'color', 'long', 'ulong', 'datetime', 'float', 'double',
    'string',
)
