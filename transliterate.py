# long summary :-
# The script first imports the required modules, including http.client, nltk, and pandas. It also downloads the WordNetLemmatizer from the Natural Language Toolkit (nltk) to perform lemmatization on the input text.
# Next, the script prompts the user to input the text that they want to transliterate. The input text is then split into individual words, and each word is lemmatized using the WordNetLemmatizer.

# The script contains a dictionary called lang_maps that maps language names to their corresponding language codes used by Google Input Tools. The translit class takes a language name as an argument and initializes a lang attribute with the corresponding language code.

# The translit class also defines two methods: request and get_lang. The request method takes a query q and a language lang and sends a GET request to Google Input Tools API to obtain the transliterated output for the query text in the specified language. The get_lang method takes a string as input and returns the corresponding transliterated output using the request method.

# The convert method of the translit class takes a list of lemmatized words as input and iterates over each word to get its corresponding transliterated output using the get_lang method. The method then concatenates the transliterated words to form a final string of transliterated text.

# Finally, the script creates a translit object with the specified language (default is Hindi), calls the convert method on the list of lemmatized words, and joins the resulting list of transliterated words into a single string. This string is then saved to a CSV file called "output.csv" using pandas DataFrame.


# -----------------------short summary :----------------------------------------
#       1. First the answer given by the student is converted manually typed in english but in hindi phonetic just like how we write in whatsapp.
#       2. Then we split the particular sentence by 'space' and store it in a list and pass it through a lemmetizer
#       3. The lemmetizer helps to find the lemme word [Lemmatisation (or lemmatization) in linguistics is the process of grouping together the inflected forms of a word so they can be analysed as a single item, identified by the word's lemma, or dictionary form.]
#       4. Then we pass all the words that we stored in a list and feed it to the translit function by default the language option here is hindi
#       5.  The translit class returns the word by word mapping of hindi words and then we join the words to make a sentence and store it in a dataframe which converts it into a csv

# ------------------------------------------------------------------
# importing the packages ----------- note all the packages depenedencies are in the requirements.txt

import pandas as pd
from nltk.stem import WordNetLemmatizer
import http.client
import nltk
# Download WordNetLemmatizer from NLTK

nltk.download('wordnet')



# Define input text prompt and split input text into individual words

text = str(input("Enter text baba  \n"))
text1 = text.split(' ')
# Instantiate WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Lemmatize input text and store in a new list

lem_text = []

for i in text1:
    l = lemmatizer.lemmatize(i)
    # print(l)
    lem_text.append(l)

# Define a dictionary to map language names to language codes used by Google Input Tools

lang_maps = {
    "hindi": "hi-t-i0-und",
    "telegu": "te-t-i0-und",
    "bengali": "bn-t-i0-und",
    "tamil": "ta-t-i0-und",
    "malayalam": "ml-t-i0-und",
    "sanskrit": "sa-t-i0-und",
    "kannada": "kn-t-i0-und",
    "gujarati": "gu-t-i0-und",
    "marathi": "mr-t-i0-und",
    "odiya": "or-t-i0-und",
    "punjabi": "pu-t-i0-und",
    "urdu": "ur-t-i0-und",
}
# Define transliteration class


class translit:
    def __init__(self, lang="hindi"):
        #   """
        # Initializes the transliteration class with the specified language.
        
        # Args:
        #     lang (str): The language to transliterate to. Defaults to Hindi.
        # """
        self.lang = lang_maps[lang]

    @staticmethod
    def request(q, lang):
        #   """
        # Sends a GET request to the Google Input Tools API to obtain the transliterated output for the query text in the specified language.

        # Args:
        #     q (str): The query text to transliterate.
        #     lang (str): The language code to transliterate to.

        # Returns:
        #     The GET response from the Google Input Tools API.
        # """
        conn = http.client.HTTPSConnection("inputtools.google.com")
        conn.request(
            "GET",
            "/request?text="
            + q
            + "&itc="
            + lang
            + "&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test",
        )
        res = conn.getresponse()
        return res

    def get_lang(self, q):
        # """
        # Returns the transliterated output for the input text in the specified language.

        # Args:
        #     q (str): The input text to transliterate.

        # Returns:
        #     The transliterated output of the input text.
        # """
        output = ""
        res = self.request(q, self.lang)
        res = res.read()
        output = str(res, encoding="utf=8")[14 + 4 + len(q): -31]
        output = output.strip()
        return output

    def convert(self, stops):
        #  """
        # Converts the input list of lemmatized words to transliterated text in the specified language.

        # Args:
        #     stops (list): The list of lemmatized words to transliterate.

        # Returns:
        #     The final string of transliterated text.
        # """
        final_list = []
        special_chars = "/.,><?][}{)(|;:-+="
        for i in range(len(stops)):
            t_word = ""
            phrase_list = stops[i][:].split(" ")
            for word in phrase_list:
                if type(word) == int:
                    t_word += word
                elif word in special_chars:
                    t_word += word
                else:
                    t_word += self.get_lang(word)
                t_word += " "
            final_list.append(t_word[:-1])
        return final_list

# Create an instance of the translit class with the target language (here, Hindi)
p = translit("hindi")
# Convert the lemmatized text to the target language using the convert function of the translit class
new_list = p.convert(lem_text)
# print(new_list)
# Join the list of converted words into a single string
mystring = ' '.join(map(str, new_list))

print(mystring)
data = {"final": mystring}
# Save the output string in a CSV file named "output.csv"
df = pd.DataFrame([data])
# print("the file is saved as {}".format(name))
df.to_csv("output.csv")





# in conclusion :
# The above code first creates an instance of the translit class with the target language as Hindi.
# It then uses the convert function of the translit class to convert the lemmatized text to the target language.
# The resulting converted words are then joined into a single string using the join function.
# Finally, the output string is saved in a CSV file named "output.csv".