from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ._tokenizer_exceptions_list import ID_BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc


# Daftar singkatan dan Akronim dari:
# https://id.wiktionary.org/wiki/Wiktionary:Daftar_singkatan_dan_akronim_bahasa_Indonesia#A

_exc = {}

for orth in ID_BASE_EXCEPTIONS:
    _exc[orth] = [{ORTH: orth}]
    orth_title = orth.title()
    _exc[orth_title] = [{ORTH: orth_title}]
    orth_caps = orth.upper()
    _exc[orth_caps] = [{ORTH: orth_caps}]
    orth_lower = orth.lower()
    _exc[orth_lower] = [{ORTH: orth_lower}]
    orth_first_upper = orth[0].upper() + orth[1:]
    _exc[orth_first_upper] = [{ORTH: orth_first_upper}]
    if "-" in orth:
        orth_title = "-".join([part.title() for part in orth.split("-")])
        _exc[orth_title] = [{ORTH: orth_title}]
        orth_caps = "-".join([part.upper() for part in orth.split("-")])
        _exc[orth_caps] = [{ORTH: orth_caps}]

for exc_data in [
    {ORTH: "Jan.", NORM: "Januari"},
    {ORTH: "Feb.", NORM: "Februari"},
    {ORTH: "Mar.", NORM: "Maret"},
    {ORTH: "Apr.", NORM: "April"},
    {ORTH: "Jun.", NORM: "Juni"},
    {ORTH: "Jul.", NORM: "Juli"},
    {ORTH: "Agu.", NORM: "Agustus"},
    {ORTH: "Ags.", NORM: "Agustus"},
    {ORTH: "Sep.", NORM: "September"},
    {ORTH: "Okt.", NORM: "Oktober"},
    {ORTH: "Nov.", NORM: "November"},
    {ORTH: "Des.", NORM: "Desember"},
]:
    _exc[exc_data[ORTH]] = [exc_data]

_other_exc = {
    "do'a": [{ORTH: "do'a", NORM: "doa"}],
    "jum'at": [{ORTH: "jum'at", NORM: "Jumat"}],
    "Jum'at": [{ORTH: "Jum'at", NORM: "Jumat"}],
    "la'nat": [{ORTH: "la'nat", NORM: "laknat"}],
    "ma'af": [{ORTH: "ma'af", NORM: "maaf"}],
    "mu'jizat": [{ORTH: "mu'jizat", NORM: "mukjizat"}],
    "Mu'jizat": [{ORTH: "Mu'jizat", NORM: "mukjizat"}],
    "ni'mat": [{ORTH: "ni'mat", NORM: "nikmat"}],
    "raka'at": [{ORTH: "raka'at", NORM: "rakaat"}],
    "ta'at": [{ORTH: "ta'at", NORM: "taat"}],
}

_exc.update(_other_exc)

for orth in [
    "A.AB.",
    "A.Ma.",
    "A.Md.",
    "A.Md.Keb.",
    "A.Md.Kep.",
    "A.P.",
    "B.A.",
    "B.Ch.E.",
    "B.Sc.",
    "Dr.",
    "Dra.",
    "Drs.",
    "Hj.",
    "Ka.",
    "Kp.",
    "M.AB",
    "M.Ag.",
    "M.AP",
    "M.Arl",
    "M.A.R.S",
    "M.Hum.",
    "M.I.Kom.",
    "M.Kes,",
    "M.Kom.",
    "M.M.",
    "M.P.",
    "M.Pd.",
    "M.Psi.",
    "M.Psi.T.",
    "M.Sc.",
    "M.SArl",
    "M.Si.",
    "M.Sn.",
    "M.T.",
    "M.Th.",
    "No.",
    "Pjs.",
    "Plt.",
    "R.A.",
    "S.AB",
    "S.AP",
    "S.Adm",
    "S.Ag.",
    "S.Agr",
    "S.Ant",
    "S.Arl",
    "S.Ars",
    "S.A.R.S",
    "S.Ds",
    "S.E.",
    "S.E.I.",
    "S.Farm",
    "S.Gz.",
    "S.H.",
    "S.Han",
    "S.H.Int",
    "S.Hum",
    "S.Hut.",
    "S.In.",
    "S.IK.",
    "S.I.Kom.",
    "S.I.P",
    "S.IP",
    "S.P.",
    "S.Pt",
    "S.Psi",
    "S.Ptk",
    "S.Keb",
    "S.Ked",
    "S.Kep",
    "S.KG",
    "S.KH",
    "S.Kel",
    "S.K.M.",
    "S.Kedg.",
    "S.Kedh.",
    "S.Kom.",
    "S.KPM",
    "S.Mb",
    "S.Mat",
    "S.Par",
    "S.Pd.",
    "S.Pd.I.",
    "S.Pd.SD",
    "S.Pol.",
    "S.Psi.",
    "S.S.",
    "S.SArl.",
    "S.Sn",
    "S.Si.",
    "S.Si.Teol.",
    "S.SI.",
    "S.ST.",
    "S.ST.Han",
    "S.STP",
    "S.Sos.",
    "S.Sy.",
    "S.T.",
    "S.T.Han",
    "S.Th.",
    "S.Th.I" "S.TI.",
    "S.T.P.",
    "S.TrK",
    "S.Tekp.",
    "S.Th.",
    "Prof.",
    "drg.",
    "KH.",
    "Ust.",
    "Lc",
    "Pdt.",
    "S.H.H.",
    "Rm.",
    "Ps.",
    "St.",
    "M.A.",
    "M.B.A",
    "M.Eng.",
    "M.Eng.Sc.",
    "M.Pharm.",
    "Dr. med",
    "Dr.-Ing",
    "Dr. rer. nat.",
    "Dr. phil.",
    "Dr. iur.",
    "Dr. rer. oec",
    "Dr. rer. pol.",
    "R.Ng.",
    "R.",
    "R.M.",
    "R.B.",
    "R.P.",
    "R.Ay.",
    "Rr.",
    "R.Ngt.",
    "a.l.",
    "a.n.",
    "a.s.",
    "b.d.",
    "d.a.",
    "d.l.",
    "d/h",
    "dkk.",
    "dll.",
    "dr.",
    "drh.",
    "ds.",
    "dsb.",
    "dst.",
    "faks.",
    "fax.",
    "hlm.",
    "i/o",
    "n.b.",
    "p.p." "pjs.",
    "s.d.",
    "tel.",
    "u.p.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
