from flask import Blueprint, request, jsonify


idea_bp = Blueprint("idea", __name__)

@idea_bp.route("/generate", methods=["POST"])
def generate_idea():
    data = request.json
    
   
    skills = data.get('skills', '').lower()
    budget = int(data.get('budget', 0))
    location = data.get('location', '').lower()

   
  
    business_repository = [
        {"name": "E-commerce Agency", "skills": "marketing", "min_budget": 500},
        {"name": "Local Delivery Service", "skills": "logistics", "min_budget": 1000},
        {"name": "Technical Consulting", "skills": "coding", "min_budget": 0},
        {"name": "Cloud Kitchen", "skills": "cooking", "min_budget": 2000}
    ]

    
    matched_ideas = [
        biz['name'] for biz in business_repository 
        if biz['skills'] in skills and budget >= biz['min_budget']
    ]

    
    if not matched_ideas:
        matched_ideas = ["General Service Consulting", "Online Dropshipping"]

    return jsonify({
        "status": "success",
        "analysis_type": "Data-Driven Matching",
        "ideas": matched_ideas[:3] 
    })
