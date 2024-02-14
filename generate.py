import sqlite3
from random import randint

# Replace with the path to your SQLite database file
db_path = '/home/kali/Desktop/sqlite_proj/cpge.db'

# Establish a connection to SQLite
con = sqlite3.connect(db_path)
cur = con.cursor()

math_topics = ["Ensembles_et_applications", "Équations_différentielles_linéaires", "Nombres_complexes", "Matrices_et_systèmes_linéaires", "Nombres_réels_et_suites_numériques", "Polynômes_et_fractions", "Fcts_réelles_d_une_variable_réelle_Limites", "Groupe_symétrique", "Fonctions_dérivées", "Déterminants", "Fonctions_convexes_Fonctions_usuelles", "Intégration_sur_un_segment", "Développements_limités", "Intégration_sur_un_intervalle_quelconque", "Structures_algébriques", "Espaces_préhilbertiens_réels", "Arithmétique_élémentaire", "Espaces_euclidiens", "Ensembles_finis", "Séries_numériques", "Espaces_vectoriels",  "Espaces_préhilbertiens", "Probabilités_et_Variables_Aléatoires", "Calcul_différentiel", "équations_différentielles", "Séries_entières", "Suites_et_séries_de_fonctions", "Fonctions_vectorielles", "Séries_dans_un_EVN"]
phys_topics = ["ELECTRONIQUE", "MECANIQUE_DE_POINT", "MECANIQUE_DE_SOLIDE", "ONDES_ELECTROMAGNETIQUES", "OPTIQUE_ONDULATOIRE", "THERMODYNAMIQUE", "PHYSIQUE_QUANTIQUE", "ELECTROCINETIQUE", "OPTIQUE_GEOMETRIQUE", "ELECTROMAGNETISME"]
chimie_topics = ["Chimie_des_solutions_aqueuses", "Cinétique_chimique", "Cristallographie", "Structure_de_la_matière", "Thermochimie", "Equilibres_binaires", "Oxydo_Réduction", "Diagramme_d_Ellingham", "Diagramme_EpH"]



def generate_math():
	cur.execute("select * from math")
	math_ = cur.fetchall()
	math_ = list(math_[0])
	m_max = max(math_)
	m_min = min(math_)
	ind_m = math_.index(m_max)
	rand_m = randint(0, len(math_topics))
	while rand_m == ind_m and m_max-m_min > 3:
		rand_m = randint(0, len(math_topics))
	new_result = math_[rand_m] +1
	cur.execute(f"update math set {math_topics[rand_m]} = {new_result};")
	print(math_topics[rand_m])
	

def generate_phys():
	cur.execute("select * from phys")
	phys_ = cur.fetchall()
	phys_ = list(phys_[0])
	p_max = max(phys_)
	p_min = min(phys_)
	ind_p= phys_.index(p_max)
	rand_p = randint(0, len(phys_topics))
	while rand_p == ind_p and p_max-p_min > 3:
		rand_p = randint(0, len(phys_topics))
	new_result = phys_[rand_p] +1
	cur.execute(f"update math set {phys_topics[rand_p]} = {new_result};")
	print(phys_topics[rand_m])


def generate_chimie():
	cur.execute("select * from chimie")
	chimie_ = cur.fetchall()
	chimie_ = list(chimie_[0])
	c_max = max(chimie_)
	c_min = min(chimie_)
	ind_c = chimie_.index(p_max)
	rand_c = randint(0, len(chimie_topics))
	while rand_c == ind_c and c_max-c_min > 3:
		rand_c = randint(0, len(chimie_topics))
	new_result = chimie_[rand_c] +1
	cur.execute(f"update chimie set {chimie_topics[rand_c]} = {new_result};")
	print(chimie_topics[rand_m])
	

generate_math()
generate_phys()
generate_chimie()


con.commit()
con.close()

