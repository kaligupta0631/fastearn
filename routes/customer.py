from flask import Blueprint, request, jsonify

customer_bp = Blueprint("customer", __name__)

@customer_bp.route("/discover", methods=["POST"])
def discover_customers():
    data = request.json
    idea = data.get('idea', '').lower()
    location = data.get('location', '').lower()

    market_segments = {
        "finance": {
            "segments": ["University Students", "Early Career Professionals", "Gig Workers"],
            "channels": ["Social Media Ads", "Campus Partnerships", "Financial Literacy Blogs"]
        },
        "food": {
            "segments": ["Busy Office Workers", "Health-Conscious Parents", "Local Residents"],
            "channels": ["Local SEO", "Food Delivery Apps", "Community Influencers"]
        },
        "tech": {
            "segments": ["Small Business Owners", "Freelancers", "Tech Enthusiasts"],
            "channels": ["LinkedIn Outreach", "Software Review Sites", "Tech Forums"]
        }
    }

    selected_category = "tech"
    for category in market_segments:
        if category in idea:
            selected_category = category
            break

    result = market_segments[selected_category]

    return jsonify({
        "status": "success",
        "location_context": location,
        "target_segments": result["segments"],
        "acquisition_channels": result["channels"]
    })