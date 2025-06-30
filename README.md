# 🍴 NOMADish - Global Foodie Tour Planner

A powerful Julep workflow that creates personalized, weather-aware culinary adventures for any city in the world. Discover iconic local dishes, find top-rated restaurants, and get complete one-day foodie tour itineraries with breakfast, lunch, and dinner recommendations.

## ✨ What This Does

NOMADish automatically:

- **Checks Weather Conditions**: Suggests indoor/outdoor dining based on current weather
- **Discovers Iconic Dishes**: Finds 3 signature local dishes per city that represent culinary heritage
- **Recommends Top Restaurants**: Provides specific restaurant names and locations
- **Creates Complete Itineraries**: Structured breakfast → lunch → dinner format
- **Adds Cultural Context**: Rich narratives explaining the significance of each dish
- **Accommodates Dietary Needs**: Supports vegetarian, vegan, gluten-free, halal, kosher diets
- **Respects Budget Preferences**: Options from budget-friendly to luxury dining

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Julep API account (free tier available)

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd NOMADish
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**

- `julep>=1.0.0` - Julep AI workflow engine
- `pyyaml>=6.0` - YAML configuration parsing
- `requests>=2.31.0` - HTTP requests
- `python-dotenv>=1.0.0` - Environment variable management

### 3. Set Up Julep API Key

Get your free API key from [Julep](https://julep.ai) and set it as an environment variable:

**Option A: Command Line**

```bash
export JULEP_API_KEY="your_julep_api_key_here"
```

**Option B: Create .env file**

```bash
echo "JULEP_API_KEY=your_julep_api_key_here" > .env
```

### 4. Run Your First Foodie Tour

```bash
python run_foodie_tour.py
```

This will generate a default tour for **Tokyo and Istanbul** with **vegetarian** preferences and **mid-range** budget.

## 📋 Configuration Options

### Cities (1-3 cities maximum)

- **Default**: `["Tokyo", "Istanbul"]`
- **Examples**:
  - Single city: `["Paris"]`
  - Two cities: `["New York", "San Francisco"]`
  - Three cities: `["Bangkok", "Mumbai", "Seoul"]`

### Dietary Preferences

- **Options**: `["vegetarian", "vegan", "gluten-free", "halal", "kosher", "none"]`
- **Default**: `["vegetarian"]`
- **Multiple options**: `["vegetarian", "gluten-free"]`

### Budget Levels

- **Options**: `["budget", "mid-range", "upscale", "luxury"]`
- **Default**: `"mid-range"`

## 🛠️ Custom Usage Examples

### Example 1: Luxury European Tour

```python
from run_foodie_tour import run_foodie_tour

result = run_foodie_tour(
    cities=["Paris", "Rome"],
    dietary_preferences=["none"],
    budget_level="luxury"
)
```

### Example 2: Vegan Asian Adventure

```python
result = run_foodie_tour(
    cities=["Bangkok", "Seoul"],
    dietary_preferences=["vegan"],
    budget_level="budget"
)
```

### Example 3: Single City Deep Dive

```python
result = run_foodie_tour(
    cities=["Mumbai"],
    dietary_preferences=["halal", "vegetarian"],
    budget_level="upscale"
)
```

## 📖 How to Run

### Method 1: Default Configuration

```bash
python run_foodie_tour.py
```

### Method 2: Edit the Script

Open `run_foodie_tour.py` and modify the main function:

```python
def main():
    # Customize these parameters
    result = run_foodie_tour(
        cities=["Your", "Preferred", "Cities"],
        dietary_preferences=["your_preferences"],
        budget_level="your_budget"
    )
```

### Method 3: Python Interactive Session

```python
python3
>>> from run_foodie_tour import run_foodie_tour
>>> result = run_foodie_tour(cities=["London"], budget_level="luxury")
```

## 📊 Understanding the Output

### Console Output

During execution, you'll see:

```
🍴 Welcome to the Global Foodie Tour Planner! 🌍
✅ API key found: sk-xxxxxxxx...
🤖 Creating Global Foodie Tour Agent...
✅ Agent created with ID: agent_xxxxxxxxx
📋 Loading task configuration...
📝 Creating foodie tour task...
✅ Task created with ID: task_xxxxxxxxx
🍽️ Executing foodie tour workflow...
🚀 Starting foodie tour planning for: Tokyo, Istanbul
📋 Dietary preferences: vegetarian
💰 Budget level: mid-range
⏳ Processing your foodie tour...
🎉 Execution completed successfully!
```

### Generated Files

Results are automatically saved as JSON files:

- **Format**: `foodie_tour_results_[timestamp].json`
- **Example**: `foodie_tour_results_1751280194.json`
- **Location**: Same directory as the script

### Sample Output Format

```
🍴 GLOBAL FOODIE TOUR GUIDE 🌍

Cities: Tokyo, Istanbul
Dietary Preferences: vegetarian
Budget Level: mid-range
Generated: Today

═══════════════════════════════════════════════════════════════

🏙️ TOKYO CULINARY ADVENTURE

🌅 BREAKFAST: Natto Toast
📍 Restaurant: Ain Soph. Journey, Shinjuku
🍽️ Description: Start your day with a delightful spin on traditional Japanese breakfast...
☁️ Weather Note: If it's sunny, enjoy your meal outside on the terrace...

🍽️ LUNCH: Shiitake Mushroom Sushi
📍 Restaurant: Sushi Zanmai, Tsukiji
🍽️ Description: Dive into the world of sushi with a fresh, vegetarian take...
☁️ Weather Note: The restaurant's bright indoor seating is fantastic...

🌙 DINNER: Vegetable Tempura with Dipping Sauce
📍 Restaurant: Tempura Kondo, Ginza
🍽️ Description: For dinner, indulge in a culinary masterpiece...
☁️ Weather Note: The elegant and warm ambiance makes it ideal...

💡 Local Tips:
- Reservations Recommended: Especially for dinner at popular spots!
- Try a Variety: Opt for tasting menus to explore diversity of flavors
- Dining Etiquette: Say "Itadakimasu" before eating
- Best Times to Visit: Lunchtime offers bento specials
```

## 📁 Project Structure

```
NOMADish/
├── 🐍 run_foodie_tour.py           # Main execution script
├── 📋 foodie_tour.yaml             # Julep workflow configuration
├── 📄 requirements.txt             # Python dependencies
├── 📖 README.md                    # This documentation
├── 🔧 .gitignore                   # Git ignore rules
├── 📊 foodie_tour_results_*.json   # Generated tour guides (auto-created)
└── 🌐 .env                         # Environment variables (optional)
```

## ⏱️ Performance & Timing

- **Average execution time**: 30-60 seconds
- **Model used**: GPT-4o-mini (optimized for speed)
- **Parallel processing**: Multiple cities processed simultaneously
- **Maximum timeout**: 3-4 minutes for safety

## 🔧 Troubleshooting

### Common Issues

**❌ "JULEP_API_KEY not found"**

```bash
# Solution: Set your API key
export JULEP_API_KEY="your_actual_api_key"
```

**❌ "ModuleNotFoundError: No module named 'julep'"**

```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**❌ "Execution taking longer than expected"**

- Check your internet connection
- Verify API key is valid
- Try with fewer cities (1 instead of 3)

**❌ "API key invalid"**

- Verify your Julep API key at [julep.ai](https://julep.ai)
- Ensure no extra spaces in the key
- Try regenerating the API key

### Debug Mode

For detailed debugging, modify the script to print more information:

```python
# Add this line after creating the execution
print(f"Execution status: {execution.status}")
print(f"Execution details: {execution}")
```

## 💡 Pro Tips for Best Results

### 🍽️ Culinary Tips

- **Mix budgets**: Try "mid-range" for varied experiences
- **Cultural immersion**: Choose "none" for dietary preferences to get authentic local dishes
- **Seasonal awareness**: The AI considers seasonal ingredients and weather

### 🌍 Travel Tips

- **Research first**: Use the generated restaurant names to check current hours
- **Make reservations**: Especially for upscale restaurants
- **Local currency**: Carry cash as some local spots may not accept cards
- **Language prep**: Learn basic food-related phrases

### 🔧 Technical Tips

- **Batch processing**: Run multiple cities separately for faster results
- **Save results**: JSON files contain complete data for future reference
- **Customize workflow**: Edit `foodie_tour.yaml` for advanced modifications

## 🌟 Example Success Stories

**Tokyo & Istanbul (Vegetarian, Mid-range)**

- Generated authentic vegetarian alternatives to traditional dishes
- Provided specific restaurant locations in popular neighborhoods
- Included cultural context and dining etiquette tips

**Paris & Rome (No restrictions, Luxury)**

- Recommended Michelin-starred establishments
- Suggested wine pairings and seasonal specialties
- Provided insider tips for reservation strategies

## 🏗️ Built With

- **[Julep](https://julep.ai)**: AI workflow orchestration platform
- **Python 3.7+**: Core application language
- **GPT-4o-mini**: Fast, efficient AI model for content generation
- **YAML**: Human-readable workflow configuration

---

**🍽️ Ready to explore the world through food? Start your culinary adventure today!**

_Happy eating! 🥘🍜🍲🍱🌮🍕_
