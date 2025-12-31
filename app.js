const API_URL = 'http://localhost:5000';

function formatMoney(num) {
    return '₹' + num.toLocaleString('en-IN');
}

function hideForm() {
    document.getElementById('businessForm').style.display = 'none';
    document.getElementById('loader').classList.remove('hide');
}

function showForm() {
    document.getElementById('businessForm').style.display = 'block';
    document.getElementById('loader').classList.add('hide');
}

async function callAPI(endpoint, data) {
    const response = await fetch(API_URL + endpoint, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    return await response.json();
}

document.getElementById('businessForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        idea: document.getElementById('idea').value,
        industry: document.getElementById('industry').value,
        budget: parseInt(document.getElementById('budget').value),
        market: document.getElementById('market').value,
        timeline: parseInt(document.getElementById('timeline').value)
    };

    hideForm();

    try {
        const ideaRes = await callAPI('/api/idea/validate', {
            idea: formData.idea,
            industry: formData.industry,
            target_market: formData.market
        });

        const roadmapRes = await callAPI('/api/roadmap/generate', {
            idea: formData.idea,
            timeline: formData.timeline,
            budget: formData.budget
        });

        const financeRes = await callAPI('/api/finance/calculate', {
            budget: formData.budget,
            industry: formData.industry,
            business_type: formData.idea.substring(0, 100)
        });

        const customerRes = await callAPI('/api/customer/analyze', {
            target_market: formData.market,
            industry: formData.industry,
            idea: formData.idea
        });

        const allData = {
            form: formData,
            idea: ideaRes,
            roadmap: roadmapRes,
            finance: financeRes,
            customer: customerRes
        };

        sessionStorage.setItem('results', JSON.stringify(allData));
        window.location.href = 'dashboard.html';
    } catch (err) {
        alert('Error occurred. Please try again.');
        showForm();
    }
});

if (window.location.pathname.includes('dashboard')) {
    const data = JSON.parse(sessionStorage.getItem('results'));
    
    if (!data) {
        window.location.href = 'index.html';
    } else {
        document.getElementById('invest').textContent = formatMoney(data.form.budget);
        document.getElementById('revenue').textContent = formatMoney(data.finance.revenue_estimate * 12);
        document.getElementById('breakeven').textContent = data.finance.break_even_months + ' months';
        document.getElementById('score').textContent = '75/100';

        document.getElementById('fixed').textContent = formatMoney(data.finance.fixed_cost);
        document.getElementById('variable').textContent = formatMoney(data.finance.variable_cost);
        document.getElementById('monthly').textContent = formatMoney(data.finance.revenue_estimate);
        document.getElementById('profit').textContent = data.finance.break_even_months + ' months';

        document.getElementById('analysisResult').textContent = data.idea.analysis;
        document.getElementById('roadmapResult').textContent = data.roadmap.roadmap;
        document.getElementById('customerResult').textContent = data.customer.insights;
    }

    document.getElementById('downloadBtn')?.addEventListener('click', () => {
        const report = `BUSINESS ANALYSIS REPORT
========================
Budget: ${formatMoney(data.form.budget)}
Industry: ${data.form.industry}

IDEA ANALYSIS
${data.idea.analysis}

FINANCIAL PROJECTIONS
Fixed: ${formatMoney(data.finance.fixed_cost)}
Variable: ${formatMoney(data.finance.variable_cost)}
Revenue: ${formatMoney(data.finance.revenue_estimate)}
Break-even: ${data.finance.break_even_months} months

ROADMAP
${data.roadmap.roadmap}

CUSTOMER INSIGHTS
${data.customer.insights}
`;
        const blob = new Blob([report], {type: 'text/plain'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'business-report.txt';
        a.click();
    });
}