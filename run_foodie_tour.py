#!/usr/bin/env python3
"""
Global Foodie Tour Planner - Fast and Reliable Results

A Julep workflow that creates weather-aware culinary adventures by discovering 
iconic dishes, finding top-rated restaurants, and crafting delightful foodie 
tour narratives for breakfast, lunch, and dinner.
"""

import os
import time
import json
import yaml
from julep import Client

def setup_api_key():
    """Setup API key from environment"""
    api_key = os.getenv("JULEP_API_KEY")
    if api_key:
        print(f"✅ API key found: {api_key[:8]}...")
        return api_key
    else:
        print("❌ JULEP_API_KEY not found in environment")
        print("Please set your API key: export JULEP_API_KEY='your_api_key_here'")
        return None

def run_foodie_tour(cities=None, dietary_preferences=None, budget_level=None):
    """Run the foodie tour workflow with customizable parameters"""
    
    # Setup API key
    api_key = setup_api_key()
    if not api_key:
        return
    
    # Default parameters
    if cities is None:
        cities = ["Tokyo", "Istanbul"]
    if dietary_preferences is None:
        dietary_preferences = ["vegetarian"]
    if budget_level is None:
        budget_level = "mid-range"
    
    # Initialize client
    client = Client(api_key=api_key)
    
    try:
        # Create agent
        print("🤖 Creating Global Foodie Tour Agent...")
        agent = client.agents.create(
            name="Global Foodie Tour Planner",
            about="A streamlined agent that creates complete foodie tours quickly using AI knowledge",
            model="gpt-4o-mini"  # Using faster model for better performance
        )
        print(f"✅ Agent created with ID: {agent.id}")
        
        # Load task configuration
        print("📋 Loading task configuration...")
        with open('foodie_tour.yaml', 'r') as file:
            task_config = yaml.safe_load(file)
        
        # Create task
        print("📝 Creating foodie tour task...")
        task = client.tasks.create(
            agent_id=agent.id,
            **task_config
        )
        print(f"✅ Task created with ID: {task.id}")
        
        # Execute workflow
        print("🍽️ Executing foodie tour workflow...")
        
        # Input data
        input_data = {
            "cities": cities,
            "dietary_preferences": dietary_preferences,
            "budget_level": budget_level
        }
        
        print(f"🚀 Starting foodie tour planning for: {', '.join(input_data['cities'])}")
        print(f"📋 Dietary preferences: {', '.join(input_data['dietary_preferences'])}")
        print(f"💰 Budget level: {input_data['budget_level']}")
        print("=" * 60)
        
        # Create execution
        execution = client.executions.create(
            task_id=task.id,
            input=input_data
        )
        print(f"✅ Execution started with ID: {execution.id}")
        print("⏳ Processing your foodie tour...")
        
        # Wait for completion
        max_attempts = 20
        attempt = 0
        
        while attempt < max_attempts:
            try:
                result = client.executions.get(execution.id)
                
                if result.status == "succeeded":
                    print(f"\n🎉 Execution completed successfully!")
                    break
                elif result.status == "failed":
                    print(f"\n❌ Execution failed: {getattr(result, 'error', 'Unknown error')}")
                    return None
                else:
                    attempt += 1
                    if attempt <= 5:
                        print(f"📊 Status: {result.status}")
                    elif attempt % 3 == 0:
                        print(f"⏳ Status: {result.status}... (attempt {attempt}/{max_attempts})")
                    
                    time.sleep(10)
                    
            except Exception as e:
                print(f"⚠️ Error checking status: {e}")
                time.sleep(5)
                attempt += 1
        
        if attempt >= max_attempts:
            print("\n⏰ Execution is taking longer than expected.")
            try:
                result = client.executions.get(execution.id)
            except:
                print("❌ Could not retrieve results")
                return None
        
        # Display and save results
        print("\n" + "=" * 60)
        print("🎉 Foodie tour results:")
        print("=" * 60)
        
        if hasattr(result, 'output') and result.output:
            if isinstance(result.output, dict) and 'complete_foodie_guide' in result.output:
                print("\n📖 YOUR COMPLETE FOODIE TOUR GUIDE:")
                print("=" * 60)
                print(result.output['complete_foodie_guide'])
                
                # Save to file
                timestamp = int(time.time())
                filename = f'foodie_tour_results_{timestamp}.json'
                with open(filename, 'w') as f:
                    json.dump(result.output, f, indent=2)
                print(f"\n💾 Complete results saved to '{filename}'")
                
                return result.output
            else:
                print("📋 Partial results received:")
                print(result.output if result.output else "No output")
                return result.output
        else:
            print("❌ No output received")
            print(f"Status: {result.status}")
            return None
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main function with example usage"""
    print("🍴 Welcome to the Global Foodie Tour Planner! 🌍")
    print("=" * 60)
    
    # Example 1: Default tour
    print("\n🍜 Running default tour (Tokyo & Istanbul, Vegetarian, Mid-range)...")
    result = run_foodie_tour()
    
    if result:
        print("\n✅ Success! Your foodie tour has been generated.")
        
        # Example 2: Custom tour (uncomment to try)
        # print("\n🌮 Running custom tour...")
        # custom_result = run_foodie_tour(
        #     cities=["Paris", "Rome"],
        #     dietary_preferences=["none"],
        #     budget_level="upscale"
        # )

if __name__ == "__main__":
    main() 