# Language in Social Context: Bridging NLP and Sociolinguistics (ESSLLI 2024)

<b>Area:</b> Language and Computation (LaCo)

<b>Level:</b> Introductory

<b>Lecturer(s):</b> Agnieszka Faleńska and Filip Miletić

<b>Help and practical exercises:</b> Pema Gurung

<b>Course Link:</b> [click here](https://2024.esslli.eu/placeholder-programme/course-overview.html#10)

<b>Abstract:</b>
This course explores the relationship between language and society by drawing on complementary perspectives from sociolinguistics and natural language processing. It discusses variation in language use in connection with 
- (i) speakers’ sociodemographic properties such as age, gender, and socioeconomic status; 
- (ii) speakers’ patterns of interaction; and 
- (iii) the social meaning conveyed through the use of different linguistic variants. 

In bringing together NLP and sociolinguistics, we aim to establish a comparable level of depth across the disciplines. <br>
- For students already acquainted with fundamental computational linguistics, the course will provide insights into the richness of language when viewed within a broader social context.
- For students with a background in sociolinguistics, we will present examples of various computational techniques that can be used to analyze linguistic variation.
- Students with previous experience in programming will be able to run the practical exercises independently and engage with different types of attested linguistic data.

# Slides

| Day | Title                     | Slides | 
| -- | ------------------------ | ----------- |
|1| Introduction    | [Day 1](slides/day1.pdf) |
|2| Demographic factors (I) | [Day 2](slides/day2.pdf) |
|3| Demographic factors (II) |  [Day 3](slides/day3.pdf) |
|4| Language variation in interaction | [Day 4](slides/day4.pdf) |
|5| NLP applications and challenges | [Day 5](slides/day5.pdf) |

# Practical exercises

Students with previous experience in programming can run additional practical exercises and play with different types of attested linguistic data. They can either use Google Colab (recommended) or run the code locally (see instructions below).

| Day | Task                     | Dataset  | Google Colab (recommended)                                                                                                                                                                        |  Jupyter notebook  (run locally) |
| -- | ------------------------ | -----------  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| 1  | Data Analysis | [Trust Data](https://github.com/MilaNLProc/translation_bias)      | [Google Colab](https://colab.research.google.com/drive/1ctMPBupu07Nr8UsP_WuJe7VFHjjocoWE?usp=sharing)     | [Local Notebook](notebooks/Trust_Data_Analysis.ipynb) |
|2| Geographical Variability | [Twitter](http://redac.univ-tlse2.fr/corpus/canen.html) | [Google Colab](https://colab.research.google.com/drive/1Q9wdazDkoryDuld52ZzRk0UriyyjcjQH) | [Local Notebook](notebooks/TwitterData.ipynb) |
|3| Gender Variability | [Trust Data](https://github.com/MilaNLProc/translation_bias) | [Google Colab](https://colab.research.google.com/drive/1I4sUJhfr06EgE99VFy3WK0VyeOOY5SyH?usp=sharing) | [Local Notebook](notebooks/TrustData_Gender.ipynb) |
|4| Style Accomodation| [Reddit CMV](https://chenhaot.com/data/cmv/cmv.tar.bz2) | [Google Colab](https://colab.research.google.com/drive/1FBYynsBdVWUBLk-QDQE4kP8kSnfj1Y-k?usp=sharing) | [Local Notebook](notebooks/CMV_Data_Analysis.ipynb) |

## Pre-requirements for practical exercises
Basic Python knowledge: [Python tutorial](https://www.tutorialspoint.com/python/index.htm) <br>

## Running code locally
Python Installation: [Python Downloads](https://www.python.org/downloads/)

### To run the code locally instead of Google Colab

- Step1: Download all the notebooks (also available in the notebook folder)
- Step2: Open jupyter notebook through the activated env
- Step3: Follow the instructions at the top on how to download the data
- Step4: Run the notebook
  
### Virtual Enivironment Setup
To install the packages used for this project run the commands in the terminal:
- Step1: Install  ``` pip install virtualenv ``` 
- Step2: Run the command (replace the ```<version>``` with your version and ```<virtual-environment-name>``` with your choice of name)
  ```python<version> -m venv <virtual-environment-name> ``` <br>
Example: ``` python -m venv my_venv ```
- Step3: Activate the Virtual env ```source my_venv/bin/activate```
<br>Note: We will be installing all the packages to <b>my_venv</b> environment and using it further to run the code.







