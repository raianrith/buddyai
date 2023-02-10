
#Install packages by
# pipenv install openai

# to run, streamlit run buddyai.py 

# Load Libraries
import streamlit as st 
import openai

# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]


# Music, Buddy 
st.title("Welcome to Buddy.AI")
st.text("by Raian Rith")
st.header("Music, Buddy")

song_text = st.text_area(label="Enter name of a song to get suggestions for similar songs: ")
temp = st.slider("On a scale of super precise (0) to go wild AI! (1), how precise do you want the song suggestions to be?", 0.0,1.0,0.5)

# Create Radio Buttons
#output_size = st.radio(label="What kind of output do you want?",
#                       options = ["To-The-Point", "Concise", "Detailed"]
#                      )

if len(song_text)>5:
    if st.button("Generate Song Suggestions"):
    # Use GPT 3 to generate summary of article
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please provide 5 songs similar to the song titled: "+ song_text,
            max_tokens = 516,
            temperature = temp)
        
        res = response["choices"][0]["text"]
        st.info(res)

        


# Movie, Buddy 
st.header("Movie, Buddy")
movie_text = st.text_area(label="Enter name of the movie you want suggestions for: ")
mov_num = st.number_input(label="How many suggestions would you like?", min_value= 1)
movie_slider = st.slider("On a scale of super precise (0) to go wild AI! (1), how precise do you want the movie suggestions to be?", 0.0,1.0,0.5)

# Create Radio Buttons
#output_size = st.radio(label="What kind of output do you want?",
#                       options = ["To-The-Point", "Concise", "Detailed"]
#                      )
    
if len(movie_text)>5:
    if st.button("Generate Movie Suggestions"):
    # Use GPT 3 to generate summary of article
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please provide " + str(mov_num) + " movies as well as where can I stream it online, simiilar to the movie titled: "+ movie_text,
            max_tokens = 516,
            temperature = movie_slider)
        
        res = response["choices"][0]["text"]
        st.info(res)

# Movie, Buddy 
st.header("Restaurant, Buddy")

restaurant_text = st.text_area(label="Enter the address you want suggestions for: ")
#restaurant_slider = st.slider("On a scale of super precise (0) to go wild AI! (1), how precise do you want the restaurant suggestions to be?", 0.0,1.0,0.5)
rest_option = st.selectbox(label='How would you like to be contacted?',
                           options=['Top Rated', 'Indian', 'Chinese'])
# Create Radio Buttons
#output_size = st.radio(label="What kind of output do you want?",
#                       options = ["To-The-Point", "Concise", "Detailed"]
#                      )
    
if len(restaurant_text)>5:
    if st.button("Generate Restaurant Suggestions"):
    # Use GPT 3 to generate summary of article
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Name a few " + rest_option + " restaurants near: "+ restaurant_text,
            max_tokens = 516,
            temperature = 0)
        
        res = response["choices"][0]["text"]
        st.info(res)
        
# Recipe, Buddy 
st.header("Recipe, Buddy")

recipe_text = st.text_area(label="Enter the item you want a recipe for: ")
recipe_slider = st.slider("On a scale of super precise (0) to go wild AI! (1), how precise do you want the recipe suggestions to be?", 0.0,1.0,0.5)

# Create Radio Buttons
#output_size = st.radio(label="What kind of output do you want?",
#                       options = ["To-The-Point", "Concise", "Detailed"]
#                      )
    
if len(recipe_text)>5:
    if st.button("Generate Recipe and Ingredients"):
    # Use GPT 3 to generate summary of article
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please provide a list of ingredients required and recipe for the following item: "+ recipe_text,
            max_tokens = 516,
            temperature = recipe_slider)
        
        res = response["choices"][0]["text"]
        st.info(res)