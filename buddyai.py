
#Install packages by
# pipenv install openai
# Load Libraries
import streamlit as st 
import openai
import time
from streamlit_chat import message
import os
from os.path import join, dirname
from dotenv import load_dotenv
#from decouple import config
# Neew change

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

password = os.environ.get('API_KEY')
#password = config('password',default='')


#to run, streamlit run buddyai.py 



# Set the GPT-3 API key
openai.api_key = password

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Buddy.AI",
                   page_icon=":bar_chart:")

st.sidebar.image("image.png", width=300)
st.sidebar.header("Menu")
category = st.sidebar.selectbox(
   label= "Browse Buddy.AI Categories :",
    options= ['Home', 'Study Buddy', 'Job Buddy', 'Language Buddy',  'Entertainment & Food Buddy']


# Home Page
)
if category == 'Home':
    
    col4, col5,col6 = st.columns([1,7,1])
    with col4:
        st.text("")
    with col5:
        st.markdown("# Welcome to Buddy.AI ! 🤖")
    with col6:
        st.text("")
        
    
    st.caption("Discover Buddy.AI, your one-stop solution for all your daily needs. With 4 categories to choose from, you'll find the perfect buddy for every aspect of your life. From Recommendation Buddy, who'll help you find the best in entertainment, food and music, to Study Buddy, who makes studying a breeze. Need a job? Job Buddy will help you tailor your resume for maximum impact. And with Language Buddy, you'll be able to communicate with ease in any language. With all this and more in one app, it's time to start your journey with Buddy.AI!")
    st.markdown("")
    st.caption("This app was created using OpenAI by Raian Rith")
    st.markdown("")
    st.subheader("Buddy.AI offers 4 Categories: ")
    
    st.markdown("##### 1. Study Buddy")
    st.markdown("##### 2. Job Buddy")
    st.markdown("##### 3. Language Buddy")
    st.markdown("##### 4. Entertainment & Food Buddy")
    
    
    
    
    #st.markdown("Tired of getting rejections from jobs? Job Buddy will help you tailor you resume according to specific job descriptions.")
    #st.markdown("Translate words like a pro, so you can impress your foreign crush or confuse your boss (just kidding, maybe).")
    
    st.markdown("")
    st.subheader("Start using Buddy.AI by browsing through the Menu on your Left...  ⬅️ ")
    
# Recommendation Buddy

elif category == 'Entertainment & Food Buddy':
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Description | ", "Buddy.Music | ", "Buddy.Movie | ", "Buddy.Restaurant | ", "Buddy.Recipe | "])

    with tab1:
        st.markdown("### Hello there! I am your Entertainment & Food Buddy! :)")
        st.caption("Meet your new entertainment and food expert, Entertainment & Food Buddy! With a lively personality and a love for all things fun, Recommendation Buddy is here to help you discover your next favorite movie, song, restaurant, or recipe. Say goodbye to endless scrolling and indecision, as Recommendation Buddy provides personalized recommendations tailored to your taste, saves your preferences, and even includes reviews and ratings to help you make informed decisions. Let Recommendation Buddy be your ultimate guide to finding the best in entertainment and food.")
        st.text("Use Entertainment & Food Buddy by browsing through the tabs up top!")
        
    
    with tab2:
            # Music Buddy 
        
        st.title("Buddy.Music AI")
        st.caption("Introducing Music Buddy, your go-to companion for all things music! With a keen ear for great tunes and a love for discovery, Music Buddy is here to help you find the perfect soundtrack for any mood or occasion. Say goodbye to repetitive playlists and uninspiring radio stations, as Music Buddy provides personalized recommendations based on your favorites, creates playlists for different activities, and even includes lyrics, and artist information. Let Music Buddy be your musical guide and help you discover new sounds and artists you'll love.")
        
        st.header("Playlist Creater") 
        
        option = st.selectbox('Create a Playlist based on : ',
                            ('Song', 'Genre', 'Mood'))
        
        if option == "Song":
            
            song_text = st.text_area(label="Enter name of a song to get suggestions for similar songs: ")
            song_er = st.text_area("By: ")
            song_num = st.number_input(label="How many songs in the playlist would you like?", min_value= 1)
            
            if len(song_text)>1:
                if st.button("Generate Playlist!"):
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                # Use GPT 3 to generate summary of article
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide a playlist of " + str(song_num) +  " songs similar to the song titled: " + song_text +
                            " by " + song_er,
                            max_tokens = 516,
                            temperature = 0.3)
                        
                        res = response["choices"][0]["text"]
                        st.info(res)
        
        elif option == "Genre":

            genre_text = st.text_area(label="Enter a genre to get a playlist matching your genre: ")
            genre_num = st.number_input(label="How many songs in the playlist would you like?", min_value= 1)
            
            if len(genre_text)>1:
                if st.button("Generate Playlist!"):
                # Use GPT 3 to generate summary of article
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide a playlist of " + str(genre_num) +  " songs based on the following genre: " + genre_text +
                            "\n The suggestions should be by different artists.",
                            max_tokens = 516,
                            temperature = 0.5)
                            
                        res = response["choices"][0]["text"]
                        st.info(res)
                    
        elif option == "Mood":

            mood_text = st.text_area(label="Enter a mood to get a playlist matching your mood: ")
            mood_num = st.number_input(label="How many songs in the playlist would you like?", min_value= 1)
            
            if len(mood_text)>0:
                if st.button("Generate Playlist!"):
                # Use GPT 3 to generate summary of article
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide a playlist of " + str(mood_num) +  " songs based on the following mood: " + mood_text +
                            "\n The suggestions should be by different artists.",
                            max_tokens = 516,
                            temperature = 0.5)
                            
                        res = response["choices"][0]["text"]
                        st.info(res)
                
                    
        st.header("Lyrics Generator") 
        lyr_text = st.text_area(label="Enter name of a song to get lyrics for: ")
        sing_text = st.text_area(label="Enter name of a artist of the song: ")
        
        if len(lyr_text)>1:
            if st.button("Generate Lyrics"):
            # Use GPT 3 to generate summary of article
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide the lyrics in english for the following song: " + str(lyr_text) +  " by" + sing_text,
                        max_tokens = 516,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                
                


    with tab3:
        
        # Movie Buddy 
        st.text("")
        st.title("Buddy.Movie AI")
        st.caption("Introducing Movie Buddy, your ultimate film companion! With a love for all things cinema and a talent for finding the perfect flick, Movie Buddy is here to help you navigate the vast world of film. Say goodbye to endless scrolling and generic recommendations, as Movie Buddy provides personalized suggestions based on your favorite genres, moods, and previously enjoyed movies. Rating buddy also helps you find ratings of all movies till 2021.")
        st.text("")
        st.header("Movie Recommender")
        
        options = st.selectbox('Recommen Movies based on : ',
                            ('Another Movie', 'Genre', 'Mood'))
        
        if options == "Another Movie":

            movie_text = st.text_area(label="Enter name of a movie, to get suggestions for similar movies: ")
            movie_num = st.number_input(label="How many movie suggestions would you like?", min_value= 1)
            #movie_genre = st.selectbox(label = 'What genre do you preder?',
                                #options=['Comedy', 'Horror', 'Action', 'Bollywood', 'Top Rated', 'Rom-Com',
                                  #      'Romantic', 'Bollywood', 'Tollywood', 'Hollywood', 'Recent', 'Old'])

            if len(movie_text)>1:
                if st.button("Generate Movie Suggestions"):
                # Use GPT 3 to generate summary of article
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide " + str(movie_num) + " movies as well as where the movies can be streamed, which are similar to the movie titled: "+ movie_text,
                            max_tokens = 516,
                            temperature = 0.5)
                        
                        res = response["choices"][0]["text"]
                        st.info(res)
        
        elif options == "Genre":
            
            mg_text = st.text_area(label="Enter your preferred genre, to get suggestions for movies with similar genre: ")
            mg_num = st.number_input(label="How many movie suggestions would you like?", min_value= 1)
            mg_coun = st.selectbox("Which country would you like the movie to be from? ", ('Hollywood', 'Bollywood', 'French', 'Korean', 'International'))
            
            if len(mg_text)>0:
                if st.button("Generate Movie Suggestions"):
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                # Use GPT 3 to generate summary of article
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide " + str(mg_num) + " " + mg_coun + " movies as well as where the movies can be streamed for the following genre: "+ mg_text,
                            max_tokens = 516,
                            temperature = 0.5)
                        
                        res = response["choices"][0]["text"]
                        st.info(res)

        elif options == "Mood":
            
            md_text = st.text_area(label="Enter your preferred mood, to get suggestions for movies with similar mood: ")
            md_num = st.number_input(label="How many movie suggestions would you like?", min_value= 1)
            md_coun = st.selectbox("Which country would you like the movie to be from? ", ('Hollywood', 'Bollywood', 'French', 'Korean', 'International'))
            
            if len(md_text)>0:
                if st.button("Generate Movie Suggestions"):
                # Use GPT 3 to generate summary of article
                    with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                        response = openai.Completion.create(
                            engine = "text-davinci-003",
                            prompt = "Please provide " + str(md_num) + " " + md_coun + "movies as well as where the movies can be streamed for the following mood that I am currently feeling: "+ md_text,
                            max_tokens = 516,
                            temperature = 0.5)
                        
                        res = response["choices"][0]["text"]
                        st.info(res)
                    
        st.text("")
        
        st.header("Movie Ratings")
        
        
        rev_text = st.text_area(label="Enter name of a movie, to get reviews and ratings: ")
        
        if len(rev_text)>1:
            if st.button("Find Ratings"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
                # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Find reviews and ratings by movie critiques for the movie: " + str(rev_text) + "\n Then, provide ratings from the most famous movie and film review websites and platforms"+ movie_text,
                        max_tokens = 516,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
             
    with tab4:
        
        # Restaurant Buddy 
        st.text("")
        st.header("Buddy.Restaurant AI")
        st.caption("Introducing Restaurant Buddy, your new dining companion! With a love for good food and a desire to find the perfect restaurant, Restaurant Buddy is here to make your dining experiences unforgettable. Say goodbye to aimless searching and subpar dining options, as Restaurant Buddy provides personalized recommendations based on your location and cuisine preferences. Whether you're in the mood for Italian, Mexican, Chinese, or anything in between, Restaurant Buddy has you covered. ")

        rstrnt_text = st.text_area(label="Enter name of a city (EX: Appleton, Wisconsin), to get suggestions for top restaurants in that city: ")
        rstrnt_num = st.number_input(label="How many restaurant suggestions would you like?", min_value= 1)
        rstrnt_cuisine = st.selectbox(label = 'How cuisine would you like?',
                            options=['Thai', 'Chinese', 'Indian', 'Italian', 'Korea ', 'Vietnamese',
                                    'Mexican', 'American', 'Japanese', 'Cheap', 'Expensive'])

        if len(rstrnt_text)>1:
            if st.button("Generate Restaurant Suggestions"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide " + str(rstrnt_num) +  " " + rstrnt_cuisine +
                        " restaurants and their average price per meal, which are most popular in the city of: "+ rstrnt_text,
                        max_tokens = 516,
                        temperature = 0.3)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
    
    with tab5:
                   
        # Recipe Buddy 
        st.text("")
        st.header("Buddy.Recipe AI")
        st.caption("Introducing Recipe Buddy, your kitchen sidekick! With a passion for cooking and a talent for discovering new and delicious recipes, Recipe Buddy is here to take your culinary skills to the next level. Say goodbye to bland meals and boring menus, as Recipe Buddy provides personalized recipes based on your favorite dishes and ingredients. Whether you're in the mood for comfort food, exotic flavors, or something in between, Recipe Buddy has you covered. It even includes ingredient prices and step-by-step instructions, making it easy for you to cook up a storm in the kitchen. Let Recipe Buddy be your culinary guide and help you create delicious and satisfying meals for you and your loved ones.")
        
        
        recipe_text = st.text_area(label="Enter name of a dish, to get suggestions for ingridients and recipe of the dish ")
        

        if len(recipe_text)>1:
            if st.button("Generate Recipe Suggestions"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide ingridients along with their prices as well as a detailed recipe for: "+ recipe_text,
                        max_tokens = 916,
                        temperature = 0.3)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)

#Study Buddy

elif category == 'Study Buddy':
    
    sbtab1, sbtab2, sbtab3, sbtab4, sbtab5 = st.tabs(["Description  | ", "Buddy.Summarize | ", "Buddy.Rephrase | ", "Buddy.PowerPoint | ", "Buddy.Dictionary | "])

    with sbtab1:
    
        # Summarize Buddy 
        st.markdown("### Hello there! I am your Study Buddy! :)")
        st.text("")
        text ="Introducing Study Buddy, your personal study assistant! With a passion for education and a talent for making complex subjects easy to understand, Study Buddy is here to help you achieve academic success. Say goodbye to endless hours of reading and struggling to understand course material, as Study Buddy provides personalized support in four essential areas as you can see above."
        
        st.caption(text)
    
    with sbtab2:
        st.header("Buddy.Summarize AI")
        st.caption("Introducing Summary Buddy, your personal summarization assistant! With a quick mind and a passion for delivering the most essential information, Summary Buddy is here to help you save time and stay informed. Say goodbye to reading long and tedious articles, as Summary Buddy provides concise and comprehensive summaries of articles, reports, and documents. Whether you're studying for an exam, staying up to date with the latest news, or simply trying to manage your time effectively, Summary Buddy is here to make your life easier. Let Summary Buddy be your trusted companion, delivering the key takeaways and insights you need to make informed decisions and stay ahead of the curve.")

        sum_text = st.text_area(label="Enter a paragraph you would like to summarize: ")
        sum_len = st.selectbox(label = 'How detailed would you like your summary to be?',
                            options=['Concise', 'Detailed', 'Long and Detailed'])

        if len(sum_text)>1:
            if st.button("Summarize"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide a " + sum_len + " summary for the following paragraph: \n" + str(sum_text),
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
            
            
    # Rephrase Buddy 
    with sbtab3:
        st.header("Buddy.Rephrase AI")
        st.caption("Introducing Rephrase Buddy, your personal language assistant! With a flair for words and a desire to make communication clear and concise, Rephrase Buddy is here to help you express your ideas effectively. Say goodbye to awkward phrasing and confusing sentences, as Rephrase Buddy provides you with suggestions to rephrase any text you need to communicate with clarity. ")

        par_text = st.text_area(label="Enter a sentence/paragraph you would like to rephrase: ")
        par_tone = st.selectbox(label = 'Set the tone of the paragraph that you would like: ',
                            options=['Formal', 'Informal', 'Optimistic', 'Pessimistic', 'Joyful', 'Sad', 'Sincere',
                                    'Hypocritical', 'Fearful', 'Hopeful', 'Humorous', 'Serious', 'Apologetic'])
        par_add = st.selectbox(label = 'What would you like to add to your current paragraph ',
                            options=['Statistics', 'Quotes', 'few sentences for development and support', 'sentences to elaborate on the primary topic', 'conclusion sentence'])
        par_len = st.selectbox(label = 'Length of the new paragraph should be: ',
                            options=['Shorter', 'Same Length', 'Longer'])
        

        if len(par_text)>1:
            if st.button("Rephrase!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please rephrase the following paragraph with a " + str(par_tone) + " tone and add more " + par_add + " relating to the paragraph provided: \n" + par_text + "\n Please make the length of the paragraph " + par_len,
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
        
    # Powerpoint Buddy 
    with sbtab4:
    
        st.header("Buddy.PowerPoint AI")
        st.caption("Introducing PowerPoint Buddy, your ultimate presentation partner! With a creative eye and a knack for organization, PowerPoint Buddy is here to help you create engaging and effective presentations. Say goodbye to cluttered slides and boring bullet points, as PowerPoint Buddy provides you with concise and impactful bullet points to accompany any paragraph or text you provide. ")
        ppt_text = st.text_area(label="Enter a paragraph you would like to get powerpoint bulletpoints for: ")
        

        if len(ppt_text)>1:
            if st.button("Generate Bullets!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide bullet points for a power point presentation that covers all the central topics of the following paragraph: \n " + ppt_text + "\n Also provide description for each bullet point",
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                
    # Dictionary Buddy 
    with sbtab5:
        st.header("Buddy.Dictionary AI")
        st.caption("Meet Dictionary Buddy! - A comprehensive language reference that provides in-depth information about a specific word, including its definition, synonyms, antonyms, and related words. ")
        dic_text = st.text_area(label="Enter a word you would like to get definition, synonyms, antonyms, and similar words for: ")
        

        if len(dic_text)>1:
            if st.button("Explain!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide definition with example sentences for the following word: " + dic_text + "\n Also provide synonyms, antonyms, and similar words for that word. ",
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                    
elif category == 'Job Buddy':
    
    jbtab1, jbtab2, jbtab3, jbtab4, jbtab5 = st.tabs(["Description  | ", "Buddy.Email | ", "Buddy.Resume | ", "Buddy.Cover_Letter | ", "Buddy.Interview | "])

    with jbtab1:
    
        # Summarize Buddy 
        st.markdown("### Hello there! I am your Job Buddy! :)")
        st.text("")
        text ="Introducing Job Buddy, your ultimate job search companion! With a sharp focus and a passion for helping you succeed, Job Buddy is here to simplify the job search process and help you land your dream job. Say goodbye to endless hours of searching, as Job Buddy provides personalized guidance in the key areas of your job search. Choose from Buddy.Email, Buddy.Resume, Buddy.Cover Letter, and Buddy.Interview to get expert advice and resources to help you make a lasting impression on potential employers. Whether you're starting your job search, or looking to take your career to the next level, Job Buddy is here to help you succeed. Let Job Buddy be your trusted guide, leading you to success in your job search and beyond."
        st.caption(text)
    
    with jbtab2:
        st.header("Email Generator")
        st.caption("Introducing Buddy.Email, your professional email generating partner! With a sharp eye for detail and a passion for clear communication, Buddy.Email is here to help you craft emails that are polished, professional, and effective. Say goodbye to boring, generic emails, as Buddy.Email provides personalized suggestions to help you write emails that stand out and get results. Whether you're sending a follow-up, making a request, or simply catching up with a colleague, Buddy.Email is here to help you write emails that are clear, concise, and memorable. Let Buddy.Email be your email writing coach, guiding you to communicate effectively and professionally through email.")
        em_title = st.text_area(label="Enter your email title")
        em_aud = st.text_area(label="Who is the email being sent to? [Ex: Dr. Green, Fraternity Club, Students, etc.]")
        em_text = st.text_area(label="Enter short description of your email content")
        em_len = st.selectbox(label = 'Select the tone of your email: ',
                            options=["Apologetic", "Appreciative", "Casual", "Congratulatory", "Confirmatory", "Empathetic", "Formal", "Friendly", "Persuasive", "Professional", "Urgent"])

        if len(em_text)>1:
            if st.button("Generate Email!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please write an email with the following details: \n" + "Email Title: " + em_title + "\n Email Audience: " + em_aud + "\n Email Description: " + em_text + "\n Email Tone: " + em_len,
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                    
    with jbtab3:
        st.header("Resume Polisher")
        st.caption("Introducing Resume Buddy, your ultimate job search companion! Whether you're a recent graduate, an experienced professional, or seeking a career change, Resume Buddy has got you covered. With its user-friendly interface and cutting-edge algorithms, Resume Buddy helps you create a polished and professional resume that showcases your skills and achievements in the best possible light.")
        jb_desc = st.text_area(label="Copy Paste the Work/Past Experience Section from your resume:")
        jb_aud = st.text_area(label="Copy Paste the job description section from a job you are interested in:")
       
        if len(jb_desc)>1:
            if st.button("Polish my Resume!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Provide recommendation on how should I polish the work experience section of my resume according to the following details: \n" + "My Work Experience:  \n" + jb_desc + "\n A Job Description from a job I want to apply for: \n" + jb_aud,
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                    
    with jbtab4:
        st.header("Cover Letter Generator")
        st.caption("Introducing Cover Letter Buddy, your personal cover letter writing expert! A well-crafted cover letter can make the difference between landing your dream job or missing out, and Cover Letter Buddy is here to help you make that difference. With its intuitive interface and powerful writing tools, Cover Letter Buddy helps you write a professional and personalized cover letter that showcases your skills, achievements, and passion for the role you're applying for. Say goodbye to generic and bland cover letters, as Cover Letter Buddy provides you with customizable templates, relevant keywords, and expert guidance to help you make a strong impression and stand out from the crowd. Let Cover Letter Buddy be your go-to tool for writing winning cover letters and securing your next job opportunity.")
        cl_len = st.selectbox(label = 'What is the cover letter for? : ',
                            options=["Job", "Grad School", "Research Institute"])
                                     
        cl_title = st.text_area(label="Enter the position you are applying for [Ex: Data Analyst, Masters in Data Science Program, Research Analyst at MIT, etc]: ")
        cl_aud = st.text_area(label="Who is the cover letter for? [Data Science Department at Facebook, UW Madison, MIT Research Institute, etc.]")
        cl_text = st.text_area(label="Copy Paste Key Points from your Resume: (OPTIONAL)")
        cl_desc = st.text_area(label="Copy Paste the description of the Position you are applying for (OPTIONAL)")
        
        if len(cl_title)>1:
            if st.button("Generate Cover Letter!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please draft a cover letter with the following details: \n" + " Type of Cover Letter: " + cl_len + "\n Position I am applying for: " + cl_title + "\n The Cover Letter is for: " + cl_aud + "\n Position Description: " + cl_desc + "\n My Key Experiences: " + cl_text,
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                    
    with jbtab5:
        st.header("Interview Prep - er")
        st.caption("Introducing Interview Prep Buddy, your ultimate companion for nailing job interviews! With a deep understanding of the interview process and a wealth of knowledge on various industries, Interview Prep Buddy is here to help you ace your next interview. Say goodbye to nervousness and insecurity, as Interview Prep Buddy provides personalized tips and guidance on common interview questions")
        iv_ind = st.selectbox(label = 'What specific industry are you interviewing for? : ',
                            options=["Accounting", "Banking", "Construction", "Education", "Engineering", "Healthcare", "Hospitality", "Information Technology", "Law", "Marketing", "Retail", "Sales", "Telecommunications"])
                                     
        iv_title = st.text_area(label="Enter the position you are applying for [Ex: Data Analyst, Sales Analyst, Project Manager, etc]: ")
        iv_top = st.selectbox(label="Who topic would you like sample QnA for? ", options= ["Company Overview", "Education & Qualifications", "Work Experience", "Skills & Abilities", "Career Goals", "Leadership", "Teamwork", "Problem Solving", "Time Management", "Communication"])
        
        if len(iv_title)>1:
            if st.button("Generate QnA!"):
                with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = "Please provide sample interview questions with answers for the following details: \n" + " Industry: " + iv_ind + "\n Question Topic: " + iv_top,
                        max_tokens = 816,
                        temperature = 0.5)
                    
                    res = response["choices"][0]["text"]
                    st.info(res)
                    
elif category == 'Language Buddy':
    
    st.header("Translater")
    st.caption("")
    lang_title = st.text_area(label="Write something in English that you want translation for ")
        
    lang_ind = st.selectbox(label = 'What language do you want your input to be translated to? : ',
                            options=[    "Amharic",    "Arabic",    "Assyrian",    "Bengali",    "Bhojpuri",    "Burmese",    "Cantonese",    "English",    "Farsi",    "French",    "Fula",    "German",    "Gujarati",    "Hakka Chinese",    "Hausa",    "Hindi",    "Italian",    "Japanese",    "Javanese",    "Kannada",    "Korean",    "Kurdish",    "Kyrgyz",    "Maori",    "Mandarin Chinese",    "Marathi",    "Min Nan Chinese",    "Mongolian",    "Nepali",    "Oromo",    "Pashto",    "Persian",    "Punjabi",    "Portuguese",    "Russian",    "Shanghainese",    "Sindhi",    "Swahili",    "Tamil",    "Telugu",    "Thai",    "Tajik",    "Turkish",    "Uighur",    "Ukrainian",    "Urdu",    "Uzbek",    "Vietnamese",    "Wu Chinese",    "Xhosa",    "Yoruba",    "Zulu"])
        
    if len(lang_title)>1:
        if st.button("Translate!"):
            with st.spinner('Sit tight! While your buddy gets the job done for you...'):
            # Use GPT 3 to generate summary of article
                response = openai.Completion.create(
                    engine = "text-davinci-003",
                    prompt = "Please translate the the following statement to " + lang_ind + ":\n" + lang_title,
                    max_tokens = 816,
                    temperature = 0.5)
                    
                res = response["choices"][0]["text"]
                st.info(res)
                    
