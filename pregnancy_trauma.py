import streamlit as st
import pandas as pd
st.set_page_config(page_title="Pregnancy Trauma & Medication",layout="wide")
menu=["Home","Types of Pregnanacy Trauma?","Symptoms Checker","Medication Guide","Therapy Technique"]
icons=["capsule"]
choice=st.sidebar.selectbox("",menu)
#Home page
if choice=="Home":
    st.title(":blue[MaternaWell]")
    st.subheader("Pregnanacy Trauma and Medication App.")
    st.write("""        Pregnancy trauma can include a range of physical and emotional experiences, such as miscarriages, stillbirths, 
        complications during labor, and other distressing events. This app provides information on various types of pregnancy trauma, 
        their symptoms, recommended medications, therapy techniques, and advice from doctors to help manage these conditions.
    """)
    st.info("The incidence of trauma during pregnancy is around 6-8%, and when considering serious forms of trauma,"
             "it affects 3-6% of all pregnancies. ")
    st.warning("Compared to non-pregnant women," 
               "pregnant women are twice as likely to suffer severe trauma and 66% more likely to progress to death")
    st.error("Pregnant women undergo marked changes in their thoracic anatomy."
              "These modifications involve both an increase in the anteroposterior and transverse diameters of the thorax by approximately 2 centimeters and"
                "a diaphragmatic elevation of up to 4 centimeters. Therefore,"
                "technical care at the time of drainage should be reinforced")
    #Type of Pregnanacy Trauma Page.
elif choice=="Types of Pregnanacy Trauma?":
    st.header("Types of :red[Pregnancy Trauma]?")
    st.error("Trauma complicates one in 12 pregnancies, and is the leading nonobstetric cause of death among pregnant women." 
             "The most common traumatic injuries are motor vehicle crashes, assaults, falls,"
               "and intimate partner violence.")
    trauma_types={
        "Miscarriage":"Loss of a pregnancy before the 20th week.Symptoms may include:"
        "cramping ,"
        "bleeding and abdominal pain.",
        "Stillbirth": "The loss of a baby after 20 weeks of pregnancy."
         "Symptoms may include decreased fetal movement.",
        "Placental Abruption": "A condition where the placenta detaches from the uterus before childbirth."
         "Symptoms may include severe abdominal pain, bleeding, and contractions.",
        "Postpartum Hemorrhage": "Excessive bleeding following childbirth."
         "Symptoms may include heavy bleeding, low blood pressure, and dizziness.",
        "Preterm Labor": "Labor that occurs before the 37th week of pregnancy."
         "Symptoms may include contractions, backache, and changes in vaginal discharge.",
    }
    selected_trauma=st.selectbox("Select a type of pregnancy trauma to  learn more:",list(trauma_types.keys()))
    st.write(f"*{selected_trauma}:*{trauma_types[selected_trauma]}")
    #Symptoms Checker Page.
elif choice=="Symptoms Checker":
    st.header(":blue[Symptoms Checker]")
    st.write("If you are experiencing any of the following symptoms, consider seeking medical attention.")
    symptoms=st.multiselect("Select your Symptoms:",["Bleeding", "Severe Abdominal Pain", "Dizziness", "Fever", "Nausea", "Vomiting", "Decreased Fetal Movement", "Contractions", "Back Pain"])
    if symptoms:
        st.write("Based on the symptoms selected, here are some possible conditions:")
        if "Bleeding" in symptoms:
            st.write("- Possible miscarriage, placental abruption, or postpartum hemorrhage,Uterine rupture.")
        if "Severe Abdominal Pain" in symptoms:
            st.write("- Possible placental abruption or preterm labor,Abdominal Changes.")
        if "Dizziness" in symptoms:
            st.write("- Possible postpartum hemorrhage or anemia")
        if "fever" in symptoms:
            st.write("- Possible bacterial infection or Listeriosis(eating raw meat, fish and unpasteurized cheese to avoid exposure to listeria)")
        if "Nausea" in symptoms:
            st.write("- Possible Stress Fatigue, allergy from certain foods or smells")
        if "Vomiting" in symptoms:
            st.write("- Possible ulcers or gallstone or appendicitis ,migraine ")
        if "Decreased Fetal Movement" in symptoms:
            st.write("- Possible Fetal brain injury or A complication with the umbilical cord")
        if "Contractions" in symptoms:
            st.write("- Possible Ruptured membranes,Hardness of abdomen or Pressure in pelvic area")
        if "Back Pain" in symptoms:
            st.write("- Possible Weakning of the back muscles or difficulty/pain when urinating")
#Medication Guide.
elif choice=="Medication Guide":
    st.header(":blue[Medication Guide]")
    st.write("This section provides a general guide on medications that may be used to treat pregnancy trauma symptoms. Please consult a healthcare professional for personalized medical advice.")
    medications={
        "Pain Relief": ["Acetaminophen", "Ibuprofen (only under doctor guidance)", "Narcotics (under strict medical supervision)"],
        "Bleeding Control": ["Oxytocin", "Misoprostol", "Methylergonovine"],
        "Infection Prevention": ["Antibiotics (as prescribed by a doctor)"],
        "Anxiety Management": ["Counseling", "Selective Serotonin Reuptake Inhibitors (SSRIs) - use under guidance"]
    }
    medication_type=st.selectbox("Select a medication category to explore:",list(medications.keys()))
    st.write(f"*{medication_type}:*{medications[medication_type]}")
elif choice=="Therapy Technique":
    st.header(":blue[Therapy] Techniques") 
    st.write("Managing pregnancy trauma often involves a combination of medical treatment and therapy. Here are some therapy techniques suggested by healthcare professionals:")  
    therapy_technique={
                "Cognitive Behavioral Therapy (CBT)": "CBT is a common type of talk therapy that helps patients identify and change negative thought patterns. Recommended for anxiety, depression, and PTSD related to pregnancy trauma.",
        "Mindfulness-Based Stress Reduction (MBSR)": "MBSR involves mindfulness meditation and yoga to reduce stress and improve emotional well-being. Often recommended for coping with trauma and anxiety.",
        "Support Groups": "Participating in support groups with others who have experienced similar trauma can provide emotional support and reduce feelings of isolation.",
        "Psychiatric Consultation": "For severe cases of anxiety, depression, or PTSD, consulting a psychiatrist for medication and therapy options is crucial. Medications should be prescribed under strict medical supervision.",
        "Physical Therapy": "For physical recovery after traumatic childbirth, physical therapy can help with pelvic floor rehabilitation and pain management."
    }
    selected_Therapy=st.selectbox("Select a therapy technique to learn more:",list(therapy_technique.keys()))
    st.write(f"*{selected_Therapy}:*{therapy_technique[selected_Therapy]}")
    #Online therapy sessions.
    st.subheader("Online Therapy Sessions")
    st.write("Online therapy sessions can provide convenient access to mental health support from the comfort of your home. Here are some platforms that offer online therapy services:")
    online_therapy_platforms={
                "BetterHelp": "Offers a range of licensed therapists specializing in trauma, anxiety, and depression. [Visit BetterHelp](https://www.betterhelp.com)",
        "Talkspace": "Provides online therapy and counseling services with licensed therapists via text, video, or voice. [Visit Talkspace](https://www.talkspace.com)",
        "7 Cups": "Offers free emotional support through trained listeners and licensed therapists for deeper therapy needs. [Visit 7 Cups](https://www.7cups.com)",
        "Amwell": "Connects you to mental health professionals through video calls. Focuses on therapy and psychiatric care. [Visit Amwell](https://www.amwell.com)",
        "Doctor on Demand": "Provides online sessions with psychologists and psychiatrists for therapy and medication management. [Visit Doctor on Demand](https://www.doctorondemand.com)"


    }
    for platform, description in online_therapy_platforms.items():
        st.write(f"- *{platform}*: {description}")

    st.subheader("Doctor's Suggestions")
    st.write("""
        - Always consult with a healthcare provider before starting any medication or therapy.
        - Seek professional help if symptoms of anxiety, depression, or PTSD persist for more than a few weeks.
        - Consider both medical and therapeutic approaches for a holistic recovery.
    """)

# Conclusion and References section
st.sidebar.subheader("References and Resources")
st.sidebar.write("""
- [American College of Obstetricians and Gynecologists (ACOG)](https://www.acog.org)
- [World Health Organization (WHO) Pregnancy Guidelines](https://www.who.int)
- [Mayo Clinic - Pregnancy Care](https://www.mayoclinic.org)
""")








    

    







