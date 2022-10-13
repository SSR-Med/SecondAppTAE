import streamlit as st

st.title("Cálculo financiero")
st.subheader("¡Bienvenido!")
st.write("Uno de los aspectos más importantes y en el que se percibe desconocimiento en las personas, es el relacionado con la parte financiera.Esta situación se puede estar presentando debido  a que en las escuelas se aborda de una manera superficial este tema lo que lleva a que no se tenga claridad de algunos aspectos y variables que la entidades financieras valoran al momento de estudiar  o analizar una solicitud de crédito, lo que lleva a que en algunas oportunidades sean rechazada.  Por tal motivo, con esta herramienta se pretende que el usuario pueda evaluar las características de las  solicitudes de crédito y que se solicitan afectan positiva o negativamente el puntaje para tener en cuenta en  la solicitud que se está o se quiere realizar.")
st.subheader("¿Cómo funciona?")
st.write("Después de esta explicación encontrarás una serie de criterios, los cuales te pediremos que analices y los ajustes de acuerdo a tus valores. Estos filtros son:")
mark = """
* Tu grado y subgrado de préstamo asignado en tu carta de crédito. 
* El propósito de tu crédito que puede ser desde educación hasta remodalaciones para el hogar. 
* El término del préstamo (Tiempo en meses). 
* La tasa de interés que solicitas. 
* Tu dti(Riesgo asociado a que la persona asuma una deuda). 
"""
st.markdown(mark)
st.write("Luego de ajustar los filtros a tus parámetros, oprimes el botón 'Calcula tu puntaje crediticio' y automáticamente te aparecerá tu puntaje de puntaje crediticioard, se te comenta qué tan probable es que tu crédito sea aprobado y una serie de imágenes en donde te ilustramos cómo está tu puntaje con respecto al resto de la población.")
# Subgrade
subgrades = ('A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3',
                               'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3', 'G4', 'G5')
subGradeOptions = st.selectbox(
    "Elige tu subgrado de préstamo asignado en la carta de crédito", subgrades)
# Grade
grades = ("A", "B", "C", "D", "E", "F", "G")
gradeOptions = st.selectbox(
    "Elige tu grado de préstamo asignado en la carta de crédito", grades)
# Propositos
purposes = ("Automóvil", "Tarjeta de credito",
            "Consolidación de deuda", "Educación", "Mejoramiento de vivienda", "Vivienda", "Compra grande", "Razón medica", "Mudanza", "Energia renovable", "Negocio pequeño", "Vacaciones", "Boda", "Otro")
purposeOption = st.selectbox("Elige tu propósito del crédito", purposes)
# Terminos: Número de pagos del prestamo
terminos = ("36 meses", "60 meses")
terminOption = st.selectbox(
    "Elige el termino del prestamo (Número de pagos del prestamo)", terminos)
# int_rate: Tasa de interes
intRateSlider = st.slider("¿A qué tasa de interés es el crédito?",
                          min_value=5.4, max_value=26.0, step=0.1)
# dti: Relación deuda riesgo
dtiRateSlider = st.slider(
    "¿De cuánto es tu dti (Relación deuda riesgo)?", min_value=0.0, max_value=39.9, step=0.1)
# Variables para ir calculando el scorecard
intercepto = 586.2184009869178
# sub_grade
subgradeCoeficients = [46.28469435694827,
                       -6.72997232497035,
                       4.809288683789053,
                       -12.439018946099052,
                       -24.117260576973752,
                       3.106416309428642,
                       6.071980972570672,
                       9.37986839554672,
                       1.4426750372699495,
                       0.8689494916458154,
                       -1.1919675090424209,
                       -3.3105464087645866,
                       6.290092879606195,
                       12.126194646768235,
                       7.727499892653811,
                       -1.4947765150390342,
                       12.22634917686777,
                       7.3870573927641585,
                       2.336951709481417,
                       3.718315194430204,
                       19.435095466852246,
                       3.4673991530635724,
                       8.791013849020677,
                       -9.999818087052205,
                       -13.841522635714126,
                       33.939428491145065,
                       -4.407810195312984,
                       -20.567501041328672,
                       -12.437347303921086,
                       -33.16833037050195,
                       -26.081688347269843,
                       -8.816113461709316,
                       -32.310707121585935,
                       6.223343550103493,
                       0.5432858610482257]
subGradeScore = {subgrades[i]: subgradeCoeficients[i]
                 for i in range(len(subgrades))}
# Para la suma del scorecard
subgradeScoreSumar = subGradeScore[subGradeOptions]
# Grade
gradeCoeficients = [7.807731192667084,
                    20.869890206402246,
                    21.641273501222894,
                    24.1738969584822,
                    7.852167746163194,
                    -36.64156041991977,
                    -60.44187951941392]
gradeScore = {grades[i]: gradeCoeficients[i] for i in range(len(grades))}
# Para la suma del scorecard
gradeScoreSumar = gradeScore[gradeOptions]
# Proposito
purposeCoeficients = [20.335721602044444,
                      30.287474988857138,
                      18.882177216653112,
                      -85.76768087620447,
                      24.9883572692056,
                      -10.625678707720402,
                      20.691034901027255,
                      6.762417401577209,
                      -1.1394217353311384,
                      -23.057312086148297,
                      -55.196578774526,
                      19.78878405854201,
                      10.95982103587955,
                      8.352403371841687]
purposeScore = {purposes[i]: purposeCoeficients[i]
                for i in range(len(purposeCoeficients))}
# Para la suma del scorecard
purposeScoreSumar = purposeScore[purposeOption]
# Terms
termCoeficient = [-12.971777230433995, -1.7667031038454166]
termScore = {terminos[i]: termCoeficient[i]
             for i in range(len(termCoeficient))}
# Para la suma del scorecard
termScoreSumar = termScore[terminOption]
# int_rate
int_rateDiccionario = {'11.612, 13.676': 10.574514357630784,
                       '13.676, 15.74': -20.933129067439612,
                       '15.74, 17.804': -56.90236223019137,
                       '17.804, 19.868': -73.77201856367358,
                       '19.868, 21.932': -75.42654011432106,
                       '21.932, 23.996': -70.66286496833004,
                       '23.996, 26.06': -18.470252261028488,
                       '5.399, 7.484': 147.11839586110057,
                       '7.484, 9.548': 110.53799139856395,
                       '9.548, 11.612': 33.19778525332637}
# Se itera para saber en qué limite está
for intervalo in int_rateDiccionario:
    limites = list(map(float, intervalo.split(',')))
    if intRateSlider > limites[0] and intRateSlider <= limites[1]:
        intRateScoreSumar = int_rateDiccionario[intervalo]
        break
# dti
dtiDiccionario = {'-0.04, 3.999': 5.904736815287538,
                  '11.997, 15.996': 2.5002345179351675,
                  '15.996, 19.995': -5.673104321982888,
                  '19.995, 23.994': -15.740034707217081,
                  '23.994, 27.993': -18.442192876042416,
                  '27.993, 31.992': -16.607278701277842,
                  '3.999, 7.998': 14.424744867714342,
                  '31.992, 35.991': -6.702651371249669,
                  '35.991, 39.99': 17.68383995153953,
                  '7.998, 11.997': 7.913225491019478}
# Se itera para saber en qué limite está
for intervalo in dtiDiccionario:
    limites = list(map(float, intervalo.split(',')))
    if dtiRateSlider > limites[0] and dtiRateSlider <= limites[1]:
        dtiRateScoreSumar = dtiDiccionario[intervalo]
        break
scoreCard = round(intercepto+subgradeScoreSumar+purposeScoreSumar + gradeScoreSumar +
                  termScoreSumar+intRateScoreSumar+dtiRateScoreSumar)
# Por si llega a ser mayor (aunque es imposible, pero por si llega a suceder)
if scoreCard > 850:
    scoreCard = 850
elif scoreCard < 300:
    scoreCard = 300
# Encima de x porcentaje
posiciones = [538.0, 559.0, 578.0, 597.0,
              614.0, 628.0, 644.0, 667.0, 711.0]


def retornarPorcentaje():
    for i in range(8, -1, -1):
        if scoreCard > posiciones[i]:
            return (i*10)+10
    return 0


if st.button("Calcula tu puntaje crediticio"):
    st.write("Tu puntaje crediticio es de:", scoreCard)
    if scoreCard >= 594:
        st.write("Tu solicitud de crédito probablemente será aprobada.")
    else:
        st.write("Lastimosamente es improbable de que tu crédito sea aprobado.")
    st.write("Tu puntaje crediticio está encima del",
             retornarPorcentaje(), "% de los puntajes crediticios de la población.")
