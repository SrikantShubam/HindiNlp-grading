# 📚 *HindiNlp-grading*
This repository contains code for grading Hindi language proficiency tests using Natural Language Processing (NLP) techniques. 📝🧐

#🛠️ *Dependencies*
The following dependencies are required to run the code in this repository:

* Python 3.x
* NumPy
* Pandas
* scikit-learn
* spaCy
* sentence-transformers


# 🚀 Installation
To install the dependencies, run the following command:

'''
pip install -r requirements.txt
'''

# 🎯 Usage
To run the grading script, use the following command:

''' 
python finalgrade.py --input_file <path_to_input_file> --output_file <path_to_output_file>

'''


* <path_to_input_file> is the path to the input file containing the text samples to grade.
* <path_to_output_file> is the path to the output file where the grading results will be written.

# 📊 Data
The input file should be a CSV file with the following columns:

id: A unique identifier for each text sample.
student_answer: The text sample to be graded.
teacher_answer: The text sample which is be compared by the student answer.

The result file will be a CSV file with the following columns:

id: The unique identifier for each text sample.
similarity_score: The similarity between the sentences
dependency_score: The dependency similarity between the sentences.
pos_score: The parts of speech similarity between the sentences.


# 🤖 Model and Methodology
The grading script uses a pre-trained model that has been trained on a large corpus of Hindi text. The model uses various NLP techniques such as transliteration, part-of-speech tagging, semantic similarity, and dependency parsing to accurately grade the proficiency of the given text sample.

Firstly, the script uses a transliteration tool to convert the Hindi written text into Hindi Devanagari script, which makes it easier to analyze the text. Then, the script uses part-of-speech tagging to determine the grammatical structure of the text sample. Next, semantic similarity is used to compare the text sample with a set of reference texts at different proficiency levels. Finally, dependency parsing is used to analyze the syntactic structure of the text sample.

All these processes generate a score, which is then aggregated to arrive at the final predicted proficiency level of the text sample. The model is designed to provide accurate and reliable grading results.

# 👨‍💻 Contributors

[https://github.com/SrikantShubam](Srikant Shubam)     - Developer
[https://github.com/vishalbimal](Vishal Bimal Francis) - Developer

#📝 License
This project is licensed under the [https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt](MIT License). See the LICENSE file for details.
