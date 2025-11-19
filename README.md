# Retention Prediction System - Project Summary

## Overview

Developed a **machine learning solution** to predict employee attrition with **82.29% accuracy**, deployed as a production-ready **REST API** using Docker. The system enables HR teams to identify at-risk employees and implement proactive retention strategies.

---

## Problem Statement

Organizations face high costs from employee turnover including recruitment expenses, lost productivity, and decreased morale. This project creates a predictive tool to identify employees likely to leave, enabling early intervention.

---

### Technical Implementation
- **API:** Flask REST API with 4 endpoints
- **Deployment:** Docker container for portability
- **Performance:** <200ms response time, 10-20 requests/second
- **Security:** Non-root container, input validation

---

## Results

### Model Performance
| Metric | Score |
|--------|-------|
| **Accuracy** | 82.29% |
| **Precision** | 78-87% |
| **Recall (Attrition)** | 86% |
| **F1-Score** | 81-83% |

### Business Impact
-  Identifies **86% of employees at risk** of leaving
-  Enables **proactive interventions** instead of reactive responses
-  **Reduces turnover costs** (50-200% of salary per employee)
-  **Data-driven decisions** for retention strategies

---

## Deliverables

**Trained Model:** Random Forest (82.29% accuracy, 37.8 MB)  
**REST API:** 4 endpoints for predictions and monitoring  
**Docker Deployment:** One-command setup (`docker-compose up -d`)  
**Documentation:** Complete guides and API references  
**Testing Suite:** Automated validation scripts  

---

## API Endpoints

| Endpoint | Purpose | Response Time |
|----------|---------|---------------|
| `GET /health` | Health check | <10ms |
| `GET /model/info` | Model details | <50ms |
| `POST /predict` | Single prediction | ~100ms |
| `POST /predict/batch` | Batch predictions | ~3s (100 employees) |

---

## Key Insights

**Compensation matters most** - Strongest attrition predictor  
**Early career risk** - First 3 years are critical  
**Overtime impact** - Strong correlation with turnover  
**Multiple factors** - No single solution; holistic approach needed

---

## Conclusion

Successfully delivered a **production-ready ML system** that:
- Achieves **82.29% accuracy** with high recall (86%)
- Deploys in **under 10 minutes**
- Provides **actionable insights** for HR teams
- Offers **immediate ROI** through reduced turnover costs

**Model Version:** 1.0  
**Completed:** November 2025  
**Technologies:** Python • scikit-learn • Flask • Docker
