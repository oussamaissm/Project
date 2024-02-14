import sqlite3

db_path = 'cpge.db'


con = sqlite3.connect(db_path)
cur = con.cursor()

math_topics = ["Ensembles_et_applications", "Équations_différentielles_linéaires", "Nombres_complexes", "Matrices_et_systèmes_linéaires", "Nombres_réels_et_suites_numériques", "Polynômes_et_fractions", "Fcts_réelles_d_une_variable_réelle_Limites", "Groupe_symétrique", "Fonctions_dérivées", "Déterminants", "Fonctions_convexes_Fonctions_usuelles", "Intégration_sur_un_segment", "Développements_limités", "Intégration_sur_un_intervalle_quelconque", "Structures_algébriques", "Espaces_préhilbertiens_réels", "Arithmétique_élémentaire", "Espaces_euclidiens", "Ensembles_finis", "Séries_numériques", "Espaces_vectoriels",  "Espaces_préhilbertiens", "Probabilités_et_Variables_Aléatoires", "Calcul_différentiel", "équations_différentielles", "Séries_entières", "Suites_et_séries_de_fonctions", "Fonctions_vectorielles", "Séries_dans_un_EVN"]
phys_topics = ["ELECTRONIQUE", "MECANIQUE_DE_POINT", "MECANIQUE_DE_SOLIDE", "ONDES_ELECTROMAGNETIQUES", "OPTIQUE_ONDULATOIRE", "THERMODYNAMIQUE", "PHYSIQUE_QUANTIQUE", "ELECTROCINETIQUE", "OPTIQUE_GEOMETRIQUE", "ELECTROMAGNETISME"]
chimie_topics = ["Chimie_des_solutions_aqueuses", "Cinétique_chimique", "Cristallographie", "Structure_de_la_matière", "Thermochimie", "Equilibres_binaires", "Oxydo_Réduction", "Diagramme_d_Ellingham", "Diagramme_EpH"]

def create_tables():
    subjects = ["math", "phys", "chimie"]
    for subject in subjects:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {subject} ({', '.join([f'{topic} INTEGER' for topic in eval(subject+'_topics')])});")
        
def insert_val():
    subjects = [["math", len(math_topics)], ["phys", len(phys_topics)], ["chimie", len(chimie_topics)]]
    for subject in subjects:
        val = tuple([0]*subject[1])
        cur.execute(f"insert into {subject[0]} values {val};")


create_tables()
insert_val()


con.commit()
con.close()

