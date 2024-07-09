import openai

# Replace with your OpenAI API key
openai.api_key = 'your-api-key'

def get_recommendations(geography, resources, flood_risk, soil_type):
    scenario = f"""
    Geography: {geography}
    Resources: {resources}
    Flood Risk: {flood_risk}
    Soil Type: {soil_type}
    """
    
    prompt = f"""
    Based on the scenario provided below, give detailed water management recommendations including specific actions, dimensions, and requirements for farmers in Burkina Faso.
    Scenario: {scenario}
    Potential actions: Zai pits, dry spells management, stone lines, earth bounds.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in sustainable agriculture in Burkina Faso."},
            {"role": "user", "content": prompt}
        ]
    )

    recommendations = response.choices[0].message['content']
    return recommendations

def main():
    geography = "Northern Burkina Faso, semi-arid region"
    resources = "Limited access to machinery, primarily manual labor available, access to basic tools (shovels, hoes)"
    flood_risk = "Low flood risk, but prone to dry spells and occasional heavy rains"
    soil_type = "Sandy soil with low fertility"

    recommendations = get_recommendations(geography, resources, flood_risk, soil_type)
    print("Water Management Recommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()
