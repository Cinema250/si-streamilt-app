#Core packages 
import streamlit as st

#NLP Pkgs 
import spacy
from spacy_streamlit import visualize_ner
from annotated_text import annotated_text

@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_model(model_name):
    nlp = spacy.load("/Users/christelleinema/Desktop/output/model-best")
    return (nlp)

def process_text(doc):
    tokens = []
    for token in doc: 
        if token.ent_type == "Mr":
            tokens.append((token.text, "Mr", "#faa"))
        elif token.ent_type == "Mrs":
            tokens.append((token.text, "Mr", "#fda"))
        elif token.ent_type == "Miss":
            tokens.append((token.text, "Mr", "#afa"))
        else: 
            tokens.append(" " + token.text + " ")
        return tokens 


nlp = load_model("/Users/christelleinema/Desktop/output/model-best")

st.title("Using Data Science Tools to Study Smithsonian Women in Science")

st.subheader("#BecauseOfHerStory American Women's Initiative internship Project")

st.markdown("Description:")
st.write("It was customary in the 19th century to refer to a woman as Mrs. <husband name>. In fact, this title was seen as a respected title for married women. However, the system of naming women by their husbands’ names is one of the ways women and their contributions have been systematically erased from historical records. This is a #BecauseOfHerStory American Women's History Initiative summer internship project by Christelle Inema. She built a new named entity recognition machine learning model that will ensure that women referred to as Mrs. <husband's first and last name> will be identified correctly and eventually their contributions will be accurately documented as well.") #here i can explain the projecy? 

st.markdown("How to use:")
st.write("You can enter or upload your doc or txt file, the model will go through the document and identify Mr., Mrs., and Miss named entities -- depending on the entities you selected on under options.")

#Draw sidebar
st.sidebar.image("BOHS logo.png")
st.sidebar.image("DSlogo.png", width= 300)


st.sidebar.header("Options")
selected_entities = st.sidebar.multiselect("Select the entities you want to extract", ["Mr", "Mrs", "Miss"], default=["Mr", "Mrs", "Miss"])

raw_text = st.text_area ("Enter Text Here")

uploaded_file = st.file_uploader("or Upload a file", type=["doc", "txt"])
if uploaded_file is not None: 
    text_input = uploaded_file.getvalue()
    text_input = text_input.decode("utf-8")


doc = nlp(raw_text)
tokens = process_text(doc)
if st.button("Enter"):
    visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

#how do i connect the sidebar to the text. So that the side bar is going through the document




















    




