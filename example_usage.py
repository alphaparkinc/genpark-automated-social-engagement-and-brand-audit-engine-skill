"""Example usage for Social Brand Audit Engine."""
from client import SocialBrandAuditEngine

if __name__ == "__main__":
    audit = SocialBrandAuditEngine.run_audit({
        "followers": 10000,
        "avg_likes": 420,
        "avg_comments": 55,
        "posts_per_week": 4
    })
    print("Brand Health Score:", audit["brand_health_score"], "Grade:", audit["grade"])
    print("Engagement Rate:", audit["engagement_rate_pct"], "%")
