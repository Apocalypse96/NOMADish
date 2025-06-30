# 🍴 Global Foodie Tour Planner

A Julep workflow that creates weather-aware culinary adventures by discovering iconic dishes, finding top-rated restaurants, and crafting delightful foodie tour narratives for breakfast, lunch, and dinner.

## ✨ Features

- **Weather-Aware Dining**: Indoor/outdoor recommendations based on conditions
- **Iconic Local Dishes**: 3 signature dishes per city representing culinary heritage
- **Restaurant Recommendations**: Specific restaurants with locations and descriptions
- **Cultural Context**: Rich narratives with cultural significance of each dish
- **Dietary Accommodations**: Support for vegetarian, vegan, gluten-free, halal, kosher diets
- **Budget Flexibility**: Options from budget-friendly to luxury dining
- **Complete Day Itinerary**: Structured breakfast → lunch → dinner format

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install julep pyyaml
```

### 2. Set API Key

```bash
export JULEP_API_KEY="your_julep_api_key_here"
```

### 3. Run the Tour Planner

```bash
python run_foodie_tour.py
```

## 📋 Configuration Options

### Cities (1-3 cities)

- Default: `["Tokyo", "Istanbul"]`
- Examples: `["Paris", "Rome"]`, `["New York"]`, `["Bangkok", "Mumbai", "Seoul"]`

### Dietary Preferences

- Options: `["vegetarian", "vegan", "gluten-free", "halal", "kosher", "none"]`
- Default: `["vegetarian"]`

### Budget Levels

- Options: `["budget", "mid-range", "upscale", "luxury"]`
- Default: `"mid-range"`

## 🛠️ Custom Usage

```python
from run_foodie_tour import run_foodie_tour

# Custom tour example
result = run_foodie_tour(
    cities=["Paris", "Rome"],
    dietary_preferences=["none"],
    budget_level="upscale"
)
```

## 📄 Output Format

The tool generates a complete guide with:

```
🏙️ CITY CULINARY ADVENTURE

🌅 BREAKFAST: [Iconic Local Dish]
📍 Restaurant: [Specific restaurant name and area]
🍽️ Description: [Detailed, mouth-watering description with cultural context]
☁️ Weather Note: [Indoor/outdoor dining suggestion]

🍽️ LUNCH: [Signature Mid-day Specialty]
📍 Restaurant: [Specific restaurant name and area]
🍽️ Description: [Detailed, appetizing description with local significance]
☁️ Weather Note: [Venue atmosphere and weather considerations]

🌙 DINNER: [Memorable Evening Experience]
📍 Restaurant: [Specific restaurant name and area]
🍽️ Description: [Vivid description that captures the essence of local dining]
☁️ Weather Note: [Ambiance and weather-appropriate suggestions]

💡 Local Tips:
- [3-4 practical tips for dining in this city]
- [Cultural dining etiquette or customs]
- [Best times to visit restaurants]
```

## 📁 Files Structure

```
📁 Global-Foodie-Tour-Planner/
├── 🐍 run_foodie_tour.py      # Main execution script
├── 📋 foodie_tour.yaml        # Julep workflow configuration
├── 📄 requirements.txt        # Python dependencies
├── 📖 README.md              # This file
└── 📊 results/               # Generated tour guides (auto-created)
```

## 💡 Pro Tips

- **Reservations**: Always check restaurant hours and make reservations when possible
- **Cash**: Carry cash as some local spots may not accept cards
- **Local Insight**: Don't hesitate to ask locals for their secret recommendations
- **Documentation**: Take photos and notes to remember your culinary journey
- **Language**: Try to learn a few food-related phrases in the local language

## 🔧 Troubleshooting

**API Key Issues**: Make sure your `JULEP_API_KEY` environment variable is set correctly

**Timeout Issues**: The workflow is optimized for speed and should complete in under 2 minutes

**No Results**: Check your internet connection and API key validity

## 🎯 Example Output

Successfully generates complete guides like:

- Tokyo: Tamagoyaki breakfast, Yasai Ramen lunch, Kaiseki dinner
- Istanbul: Menemen breakfast, Yaprak Sarma lunch, Meze dinner
- Complete with restaurant recommendations, cultural context, and local tips

## 🏗️ Built With

- **Julep**: AI workflow orchestration
- **Python**: Core application logic
- **YAML**: Workflow configuration
- **GPT-4o-mini**: Fast, efficient AI model

---

**Happy eating! 🥘🍜🍲🍱🌮🍕**
