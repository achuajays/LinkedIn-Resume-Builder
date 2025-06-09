#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from linkedin_resume_builder.crew import LinkedinResumeBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'url': "linkedin url",
        'email': "email",
        "phone": "94756843",
        'job_description': """
                    🧾 Demo Job Description: Machine Learning Engineer
            Job Title: Machine Learning Engineer
            Location: Remote / Bangalore, India
            Company: FutureAI Technologies Pvt. Ltd.
            Employment Type: Full-time
            Experience Level: Mid to Senior (3–7 years)
            
            🔍 Job Summary:
            We are seeking a highly motivated and skilled Machine Learning Engineer to join our AI R&D team. You will design, develop, and deploy machine learning models that power real-world applications in healthcare, finance, and autonomous systems.
            
            🛠 Responsibilities:
            Design, implement, and evaluate machine learning models for various use cases.
            
            Collaborate with product teams to define data and modeling requirements.
            
            Build and maintain scalable training pipelines using tools like TensorFlow, PyTorch, and scikit-learn.
            
            Perform exploratory data analysis and feature engineering on large datasets.
            
            Optimize models for performance, accuracy, and cost-efficiency.
            
            Deploy models using cloud-based platforms (AWS/GCP/Azure).
            
            Document experiments, workflows, and results for reproducibility.
            
            ✅ Requirements:
            Bachelor’s or Master’s degree in Computer Science, Data Science, Engineering, or a related field.
            
            3+ years of experience in machine learning or applied data science.
            
            Strong programming skills in Python; familiarity with R or Java is a plus.
            
            Solid understanding of statistics, probability, and ML algorithms (SVMs, neural networks, ensembles, etc.).
            
            Experience with libraries such as TensorFlow, PyTorch, scikit-learn, and pandas.
            
            Familiarity with REST APIs, Docker, and CI/CD pipelines.
            
            Excellent problem-solving skills and attention to detail.
            
            
            """
    }
    
    try:
        LinkedinResumeBuilder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
   inputs = {
        'url': "linkedin url",
        'email': "email",
        "phone": "94756843",
        'job_description': """
                    🧾 Demo Job Description: Machine Learning Engineer
            Job Title: Machine Learning Engineer
            Location: Remote / Bangalore, India
            Company: FutureAI Technologies Pvt. Ltd.
            Employment Type: Full-time
            Experience Level: Mid to Senior (3–7 years)
            
            🔍 Job Summary:
            We are seeking a highly motivated and skilled Machine Learning Engineer to join our AI R&D team. You will design, develop, and deploy machine learning models that power real-world applications in healthcare, finance, and autonomous systems.
            
            🛠 Responsibilities:
            Design, implement, and evaluate machine learning models for various use cases.
            
            Collaborate with product teams to define data and modeling requirements.
            
            Build and maintain scalable training pipelines using tools like TensorFlow, PyTorch, and scikit-learn.
            
            Perform exploratory data analysis and feature engineering on large datasets.
            
            Optimize models for performance, accuracy, and cost-efficiency.
            
            Deploy models using cloud-based platforms (AWS/GCP/Azure).
            
            Document experiments, workflows, and results for reproducibility.
            
            ✅ Requirements:
            Bachelor’s or Master’s degree in Computer Science, Data Science, Engineering, or a related field.
            
            3+ years of experience in machine learning or applied data science.
            
            Strong programming skills in Python; familiarity with R or Java is a plus.
            
            Solid understanding of statistics, probability, and ML algorithms (SVMs, neural networks, ensembles, etc.).
            
            Experience with libraries such as TensorFlow, PyTorch, scikit-learn, and pandas.
            
            Familiarity with REST APIs, Docker, and CI/CD pipelines.
            
            Excellent problem-solving skills and attention to detail.
            
            
            """
    }
    try:
        LinkedinResumeBuilder().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LinkedinResumeBuilder().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'url': "linkedin url",
        'email': "email",
        "phone": "94756843",
        'job_description': """
                    🧾 Demo Job Description: Machine Learning Engineer
            Job Title: Machine Learning Engineer
            Location: Remote / Bangalore, India
            Company: FutureAI Technologies Pvt. Ltd.
            Employment Type: Full-time
            Experience Level: Mid to Senior (3–7 years)
            
            🔍 Job Summary:
            We are seeking a highly motivated and skilled Machine Learning Engineer to join our AI R&D team. You will design, develop, and deploy machine learning models that power real-world applications in healthcare, finance, and autonomous systems.
            
            🛠 Responsibilities:
            Design, implement, and evaluate machine learning models for various use cases.
            
            Collaborate with product teams to define data and modeling requirements.
            
            Build and maintain scalable training pipelines using tools like TensorFlow, PyTorch, and scikit-learn.
            
            Perform exploratory data analysis and feature engineering on large datasets.
            
            Optimize models for performance, accuracy, and cost-efficiency.
            
            Deploy models using cloud-based platforms (AWS/GCP/Azure).
            
            Document experiments, workflows, and results for reproducibility.
            
            ✅ Requirements:
            Bachelor’s or Master’s degree in Computer Science, Data Science, Engineering, or a related field.
            
            3+ years of experience in machine learning or applied data science.
            
            Strong programming skills in Python; familiarity with R or Java is a plus.
            
            Solid understanding of statistics, probability, and ML algorithms (SVMs, neural networks, ensembles, etc.).
            
            Experience with libraries such as TensorFlow, PyTorch, scikit-learn, and pandas.
            
            Familiarity with REST APIs, Docker, and CI/CD pipelines.
            
            Excellent problem-solving skills and attention to detail.
            
            
            """
    }
    
    try:
        LinkedinResumeBuilder().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
