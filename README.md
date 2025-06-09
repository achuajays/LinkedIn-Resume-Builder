# LinkedIn Resume Builder 🚀

![iimage.png](images/image.png)
An intelligent AI-powered system that automatically extracts professional data from LinkedIn profiles and generates tailored, professional resumes using CrewAI's multi-agent framework.

## 🌟 Features

- **Automated LinkedIn Data Extraction**: Scrapes professional information from LinkedIn profiles
- **AI-Powered Resume Generation**: Creates well-formatted, industry-standard resumes
- **Job Description Tailoring**: Customizes resumes based on specific job requirements
- **Multi-Agent Architecture**: Uses specialized AI agents for different tasks
- **Professional Formatting**: Generates clean, visually appealing resume layouts

## 🏗️ Architecture

The system uses a **multi-agent approach** with two specialized AI agents:

### 🤖 Agents

1. **Data Extraction Specialist**
   - Extracts structured data from LinkedIn profiles
   - Processes professional information including experience, education, skills, and certifications
   - Ensures data accuracy and completeness

2. **Resume Builder (Professional Resume Architect)**
   - Transforms extracted data into professional resumes
   - Tailors content based on job descriptions
   - Applies industry-standard formatting and best practices

### 🔄 Workflow

```
LinkedIn URL → Data Extraction → Resume Generation → Final Resume Output
```

## 📋 Prerequisites

- Python >= 3.10, < 3.14
- UV package manager
- Valid API keys (see setup section)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd linkedin-resume-builder
   ```

2. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

3. **Install dependencies**:
   ```bash
   crewai install
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add:
   ```env
   MODEL=your_ai_model
   GEMINI_API_KEY=your_gemini_api_key
   RAPIDAPI_KEY=your_rapidapi_key
   ```

## 🔧 Configuration

### API Keys Required

- **GEMINI_API_KEY**: For AI agents (Google Gemini)
- **RAPIDAPI_KEY**: For LinkedIn data extraction via RapidAPI
- **MODEL**: Specify your preferred AI model

### User Preferences

Edit `knowledge/user_preference.txt` to customize:
- User name
- Professional title
- Areas of interest
- Location

## 🎯 Usage

### Basic Usage

Run the resume builder with default parameters:

```bash
crewai run
```

### Custom Parameters

Modify the `inputs` dictionary in `main.py`:

```python
inputs = {
    'url': "https://www.linkedin.com/in/your-profile/",
    'email': "your.email@example.com",
    'phone': "your-phone-number",
    'job_description': """
        Your target job description here...
    """
}
```

### Available Commands

- **Run**: `crewai run` - Execute the resume building process
- **Train**: `python main.py train <iterations> <filename>` - Train the AI agents
- **Replay**: `python main.py replay <task_id>` - Replay specific tasks
- **Test**: `python main.py test <iterations> <eval_llm>` - Test the system

## 📁 Project Structure

```
linkedin_resume_builder/
├── README.md
├── knowledge/
│   └── user_preference.txt          # User customization
├── src/linkedin_resume_builder/
│   ├── __init__.py
│   ├── crew.py                      # Agent and task definitions
│   ├── main.py                      # Entry point
│   ├── config/
│   │   ├── agents.yaml             # Agent configurations
│   │   └── tasks.yaml              # Task definitions
│   └── tools/
│       ├── __init__.py
│       ├── custom_tool.py          # Custom tool template
│       └── linkedin_tool.py        # LinkedIn data extraction
└── Resume.md                       # Generated resume output
```

## 📄 Output

The system generates a professional resume in Markdown format (`Resume.md`) with the following sections:

- **Header**: Name, title, contact information
- **Experience**: Professional work history with achievements
- **Education**: Academic background
- **Skills**: Technical and professional competencies
- **Certifications**: Professional certifications and credentials

## 🛠️ Customization

### Adding New Tools

1. Create a new tool in `tools/` directory
2. Inherit from `BaseTool`
3. Define input schema and implementation
4. Add to agent configuration

### Modifying Agents

Edit `config/agents.yaml` to customize:
- Agent roles and goals
- Backstories and personalities
- Behavior parameters

### Updating Tasks

Modify `config/tasks.yaml` to change:
- Task descriptions
- Expected outputs
- Agent assignments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Join Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Chat with Documentation](https://chatg.pt/DWjSBZn)

## ⚠️ Important Notes

- Ensure you have valid API keys before running
- LinkedIn data extraction is subject to LinkedIn's terms of service
- The system requires internet connectivity for API calls
- Generated resumes should be reviewed and customized as needed

## 🔒 Privacy & Ethics

- This tool is designed for personal use to create your own resume
- Respect LinkedIn's terms of service and rate limits
- Only extract data from profiles you own or have permission to access
- Review generated content for accuracy before use

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, questions, or feedback:
- Check the [CrewAI documentation](https://docs.crewai.com)
- Visit the [GitHub repository](https://github.com/joaomdmoura/crewai)
- Join the [Discord community](https://discord.com/invite/X4JWnZnxPb)

---

**Built with ❤️ using CrewAI - Empowering AI agents to collaborate effectively**
