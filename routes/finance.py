from flask import Blueprint, request, jsonify

finance_bp = Blueprint("finance", __name__)

@finance_bp.route("/estimate", methods=["POST"])
def estimate_finance():
    data = request.json

    fixed_cost = int(data.get("fixed_cost", 50000))
    variable_cost = int(data.get("variable_cost", 20000))
    price_per_unit = int(data.get("price_per_unit", 500))
    monthly_sales = int(data.get("monthly_sales", 200))

    revenue = price_per_unit * monthly_sales
    total_monthly_cost = fixed_cost + variable_cost
    profit = revenue - total_monthly_cost

    contribution_margin = price_per_unit - (variable_cost / max(monthly_sales, 1))
    
    if contribution_margin > 0:
        break_even_units = fixed_cost / contribution_margin
        break_even_months = break_even_units / max(monthly_sales, 1)
    else:
        break_even_months = -1

    return jsonify({
        "status": "success",
        "calculations": {
            "fixed_cost": fixed_cost,
            "variable_cost": variable_cost,
            "monthly_revenue": revenue,
            "monthly_profit": profit,
            "break_even_months": round(break_even_months, 2) if break_even_months > 0 else "N/A"
        }
    })