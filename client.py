"""Automated Social Engagement & Brand Audit Engine.
100% Python Standard Library.
"""

class SocialBrandAuditEngine:
    """Audits brand social metrics, engagement velocity, and identifies content gaps."""
    
    @staticmethod
    def run_audit(profile_metrics: dict) -> dict:
        followers = max(1, profile_metrics.get("followers", 1))
        likes = profile_metrics.get("avg_likes", 0)
        comments = profile_metrics.get("avg_comments", 0)
        posts_per_week = profile_metrics.get("posts_per_week", 0)
        
        engagement_rate = round(((likes + comments * 2) / followers) * 100, 2)
        
        gaps = []
        if posts_per_week < 3:
            gaps.append("Low posting cadence (< 3 posts/week reduces algorithmic reach)")
        if comments < likes * 0.05:
            gaps.append("Low conversational depth (add open-ended questions at end of posts)")
        if engagement_rate < 2.0:
            gaps.append("Sub-benchmark engagement rate (test video demos and carousel hooks)")
            
        health_score = min(100, int(engagement_rate * 15) + min(40, posts_per_week * 8))
        
        return {
            "engagement_rate_pct": engagement_rate,
            "brand_health_score": health_score,
            "grade": "A" if health_score >= 80 else ("B" if health_score >= 60 else "C"),
            "identified_gaps": gaps
        }
