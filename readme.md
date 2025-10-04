# JOB_NAVIGATOR: An Intelligent ETL Pipeline for Job Market Analysis

JOB_NAVIGATOR is a sophisticated, containerized ETL pipeline designed to ingest raw job postings from various sources, use Natural Language Processing to understand and structure them, and load the enriched data into a standardized database schema. The project transforms messy, unstructured text into a powerful, queryable dataset for advanced job market analysis, trend identification, and data-driven insights.

## Key Features

*   **Automated Data Ingestion**: Concurrently fetches job data from public APIs of modern HR platforms like Greenhouse and Ashby.
*   **ML-Powered Transformation**: Leverages Named Entity Recognition (NER) models to extract key entities such as skills, technologies, benefits, and responsibilities directly from job descriptions.
*   **Data Standardization via Clustering**: Employs embedding and clustering algorithms to group similar extracted entities, ensuring data consistency (e.g., "AWS," "Amazon Web Services," and "aws" are all mapped to a single canonical entity).
*   **Configurable & Extensible**: Pipeline behavior, data sources, and performance parameters are controlled via external configuration files, requiring no code changes for new targets.
*   **Containerized Deployment**: Packaged with Docker for easy, consistent, and isolated deployment in any environment.

## High-Level Architecture

The pipeline follows a modular, multi-stage ETL process. Raw data is first ingested, then transformed using a series of handlers and ML models. The extracted information is clustered for standardization before being loaded into a final, structured data warehouse.

![Database Schema](./docs/Job_nav_schema.svg)

<details>
<summary><b>Click to view detailed database schema</b></summary>

*   `benefits_clusters(id, name, cluster_id)`
*   `canonical_jobs(id, job_url, active, title, description, employment_type, location, salary_min, salary_max, salary_currency, salary_interval, company_id, published_at, domain, work_setting, inserted_at)`
*   `cluster_definitions(cluster_name, member_count, source_table, last_updated, cluster_id)`
*   `companies(id, name, ats_provider, tier, slug)`
*   `domains_clusters(id, name, cluster_id)`
*   `employment_types(id, name)`
*   `etl_log(id, last_run)`
*   `job_benefits(job_id, benefit_id)`
*   `job_domains(job_id, domain_id)`
*   `job_employment_types(job_id, employment_type_id)`
*   `job_regions(job_id, region_id)`
*   `job_requirements(job_id, requirement_id, experience)`
*   `job_responsibilities(job_id, responsibility_id)`
*   `job_specializations(job_id, specialization_id)`
*   `job_tech_stacks(job_id, tech_stack_id)`
*   `job_work_settings(job_id, work_setting_id)`
*   `jobs(id, role, level, salary_min, salary_max, salary_currency, salary_interval, overall_experience, language)`
*   `regions(id, name)`
*   `requirements_clusters(id, name, cluster_id)`
*   `responsibilities_clusters(id, name, cluster_id)`
*   `specializations_clusters(id, name, cluster_id)`
*   `tech_stacks(id, name)`
*   `work_settings(id, name)`

</details>

## Technology Stack

*   **Backend**: Python
*   **ETL & Data Processing**: Pandas, Scikit-learn
*   **Machine Learning / NLP**: Hugging Face Transformers for Named Entity Recognition (NER), Sentence-Transformers for embeddings.
*   **Deployment**: Docker
*   **Database**: PostgreSQL
*   **API Interaction**: `httpx`, `asyncio`

## Project Structure

The project is organized into distinct modules, each responsible for a specific stage of the ETL process, promoting modularity and maintainability.

```
📁 JOB_NAVIGATOR/
├── 📁 docs/
│   ├── 📄 job_nav_schema.drawio   # Editable source diagram
│   └── 🖼️ job_nav_schema.svg
├── 📁 ingestor/
│   ├── 📁 clusterer/    # Handles standardization of extracted entities
│   ├── 📁 stager/       # Extracts and stages raw data from sources
│   └── 📁 transformer/    # Uses ML models to transform and structure data
├── 🐍 manage.py
├── 📄 requirements.txt
├── 🐳 Dockerfile
├── ⚙️ config.json.template  # Example configuration
└── ⚙️ .env.example          # Example environment variables
```
## Note

This is demo repository, it provides a **public stub** of job navigator, 
This version is intended for:
    - Understanding project
    -Reference for adaptation

The **full version** with implementation is **private**
To request access:
    -Email: adisrivastava027@gmail.com
    -Or contact via [linkedin](https://www.linkedin.com/in/adityansh-srivastava)