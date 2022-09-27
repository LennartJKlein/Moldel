from enum import Enum, auto


class Player(Enum):
    """ This enum contains all players that participated in 'Wie is de mol?' (if a player participated in multiple
    seasons then you need an enum value for every season in which this player participated). Furthermore ensure that
    newly added players are always added at the end of the list (even if they are from older seasons), this is related
    to the encoding of pickle. """
    ANNETTE_8 = auto()
    COEN_8 = auto()
    DENNIS_8 = auto()
    DUNYA_8 = auto()
    EDO_8 = auto()
    GEORGINA_8 = auto()
    JORIS_8 = auto()
    NICOLETTE_8 = auto()
    PATRICK_8 = auto()
    REGINA_8 = auto()
    ANNIEK_9 = auto()
    DENNIS_9 = auto()
    FROUKJE_9 = auto()
    HANS_9 = auto()
    JON_9 = auto()
    PAULA_9 = auto()
    RICK_9 = auto()
    SEBASTIAAN_9 = auto()
    VERA_9 = auto()
    VIVIENNE_9 = auto()
    ARJEN_10 = auto()
    BARBARA_10 = auto()
    ERIK_10 = auto()
    FRITS_10 = auto()
    HIND_10 = auto()
    KIM_10 = auto()
    LORETTA_10 = auto()
    MANUEL_10 = auto()
    SANNE_10 = auto()
    TIM_10 = auto()
    ANNA_11 = auto()
    ART_11 = auto()
    HANNA_11 = auto()
    HORACE_11 = auto()
    JAN_11 = auto()
    KARIN_11 = auto()
    MIRYANNA_11 = auto()
    PATRICK_11 = auto()
    PEPIJN_11 = auto()
    SOUNDOS_11 = auto()
    ANNE_MARIE_12 = auto()
    DIO_12 = auto()
    FRITS_12 = auto()
    HADEWYCH_12 = auto()
    LIESBETH_12 = auto()
    MAARTEN_12 = auto()
    MARIT_12 = auto()
    MARION_12 = auto()
    TIM_12 = auto()
    WILLIAM_12 = auto()
    CAROLIEN_13 = auto()
    DANIEL_13 = auto()
    EWOUT_13 = auto()
    JANINE_13 = auto()
    JOEP_13 = auto()
    KEES_13 = auto()
    PAULIEN_13 = auto()
    TANIA_13 = auto()
    TIM_13 = auto()
    ZARAYDA_13 = auto()
    AAF_14 = auto()
    DAPHNE_14 = auto()
    FREEK_14 = auto()
    JAN_WILLEM_14 = auto()
    JENNIFER_14 = auto()
    MAURICE_14 = auto()
    OWEN_14 = auto()
    SOFIE_14 = auto()
    SUSAN_14 = auto()
    TYGO_14 = auto()
    AJOUAD_15 = auto()
    CAROLINA_15 = auto()
    CHRIS_15 = auto()
    EVELIEN_15 = auto()
    MARGRIET_15 = auto()
    MARLIJN_15 = auto()
    MARTINE_15 = auto()
    PIETER_15 = auto()
    RIK_15 = auto()
    VIKTOR_15 = auto()
    AIREN_16 = auto()
    ANNEMIEKE_16 = auto()
    CECILE_16 = auto()
    ELLIE_16 = auto()
    KLAAS_16 = auto()
    MARJOLEIN_16 = auto()
    REMY_16 = auto()
    ROP_16 = auto()
    TAEKE_16 = auto()
    TIM_16 = auto()
    DIEDERIK_17 = auto()
    IMANUELLE_17 = auto()
    JEROEN_17 = auto()
    JOCHEM_17 = auto()
    ROOS_17 = auto()
    SANNE_17 = auto()
    SIGRID_17 = auto()
    THOMAS_17 = auto()
    VINCENT_17 = auto()
    YVONNE_17 = auto()
    BELLA_18 = auto()
    EMILIO_18 = auto()
    JAN_18 = auto()
    JEAN_MARC_18 = auto()
    LOES_18 = auto()
    OLCAY_18 = auto()
    RON_18 = auto()
    RUBEN_18 = auto()
    SIMONE_18 = auto()
    STINE_18 = auto()
    EVELIEN_19 = auto()
    EVI_19 = auto()
    JAMIE_19 = auto()
    MEREL_19 = auto()
    NIELS_19 = auto()
    NIKKIE_19 = auto()
    RICK_PAUL_19 = auto()
    ROBERT_19 = auto()
    SARAH_19 = auto()
    SINAN_19 = auto()
    ANITA_20 = auto()
    BUDDY_20 = auto()
    CLAES_20 = auto()
    JAIKE_20 = auto()
    JOHAN_20 = auto()
    LEONIE_20 = auto()
    MILJUSCHKA_20 = auto()
    NATHAN_20 = auto()
    ROB_20 = auto()
    TINA_20 = auto()
    ELLIE_21 = auto()
    HORACE_21 = auto()
    JEROEN_21 = auto()
    NADJA_21 = auto()
    NIKKIE_21 = auto()
    PATRICK_21 = auto()
    PEGGY_21 = auto()
    RON_21 = auto()
    TINA_21 = auto()
    TYGO_21 = auto()
    ALEX_7 = auto()
    DICK_7 = auto()
    EVA_7 = auto()
    INGE_7 = auto()
    LIESBETH_7 = auto()
    MENNO_7 = auto()
    NADJA_7 = auto()
    PAUL_7 = auto()
    RENATE_7 = auto()
    SANDER_7 = auto()
    CHRIS_6 = auto()
    FREDERIQUE_6 = auto()
    GEERT_6 = auto()
    LIZ_6 = auto()
    MARY_LOU_6 = auto()
    MILOUSKA_6 = auto()
    PEGGY_6 = auto()
    RICHARD_6 = auto()
    RODERICK_6 = auto()
    TOINE_6 = auto()
    GIJS_5 = auto()
    ISABELLE_5 = auto()
    JIM_5 = auto()
    LOTTIE_5 = auto()
    MARC_MARIE_5 = auto()
    ROELAND_5 = auto()
    SANDER_5 = auto()
    VICTORIA_5 = auto()
    YVON_5 = auto()
    YVONNE_5 = auto()
    CHARLOTTE_22 = auto()
    ERIK_22 = auto()
    FLORENTIJN_22 = auto()
    JOSHUA_22 = auto()
    LAKSHMI_22 = auto()
    MARIJE_22 = auto()
    REMCO_22 = auto()
    RENEE_22 = auto()
    ROCKY_22 = auto()
    SPLINTER_22 = auto()
    AAFKE_4 = auto()
    ASTRID_4 = auto()
    CHANDRIKA_4 = auto()
    ELISE_4 = auto()
    FERDI_4 = auto()
    JULIEN_4 = auto()
    LOUIS_4 = auto()
    PATRICIA_4 = auto()
    RENE_4 = auto()
    RON_4 = auto()
    DICK_3 = auto()
    ELLEN_3 = auto()
    ERIK_3 = auto()
    GEORGE_3 = auto()
    HARRY_3 = auto()
    JANTIEN_3 = auto()
    JOHN_3 = auto()
    KAREN_3 = auto()
    KERSTIN_3 = auto()
    PAMELA_3 = auto()
    PRINCE_3 = auto()
    BJORN_2 = auto()
    COR_2 = auto()
    DAN_2 = auto()
    DOORTJE_2 = auto()
    GERDA_2 = auto()
    NAZIFE_2 = auto()
    NICO_2 = auto()
    SIGRID_2 = auto()
    WARD_2 = auto()
    YVONNE_2 = auto()
    ARNOUD_1 = auto()
    DEBORAH_1 = auto()
    FOKE_1 = auto()
    JOHN_1 = auto()
    PETRA_1 = auto()
    ROBIN_1 = auto()
    SANDY_1 = auto()
    WARNER_1 = auto()
    WILLY_1 = auto()
    WILMIE_1 = auto()
    ARNO_23 = auto()
    EVERON_23 = auto()
    FRESIA_23 = auto()
    GLEN_23 = auto()
    HILA_23 = auto()
    KIM_LIAN_23 = auto()
    LAETITIA_23 = auto()
    SAHIL_23 = auto()
    SUZANNE_23 = auto()
    THOMAS_23 = auto()
    WELMOED_23 = auto()
