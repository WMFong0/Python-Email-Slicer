# Email Slicer in Python
## Overview
An **advanced Python email analyzer** that slices email addresses and provides detailed domain classification using an external database. The program now offers more comprehensive analysis with configurable domain categories.

## Key Features
- **Database-driven analysis** using ***database.csv*** for easy customization

- **Enhanced domain classification:**

  - Personal email providers (Gmail, Yahoo, Outlook, etc.)

  - Government domains (including international like .gov.hk)

  - Educational institutions (.edu)

  - Non-profit organizations (.org, .ngo)

  - Country-specific domains (50+ countries supported)

**Detailed output** showing:

  - Username and domain components

  - Email provider (for personal accounts)
  
  - Organization type (for institutional emails)

  - Country of origin (when detectable)

- **Error handling** for invalid email formats

- **Simple command-line interface**

## Database Configuration
The program uses ***database.csv*** containing:

- ***DOMAIN_CATEGORY***: TLD classifications and country codes
  
- ***COMMON_PROVIDER***: Known email service providers
  
- ***ORG_TYPE***: Organization type mappings

## How to Use
1. Ensure ***database.csv*** is in the same directory as the script
2. Run the program: python ***main.py***
3. Enter an email address when prompted
4. View the detailed analysis including:
   - Username and domain components
   - Email provider (if personal account)
   - Organization type (if institutional email)
   - Country detection (limited to popular country at the moment)
5. Press Enter with no input to exit

## Requirements

* Python 3.x (csv is build-in module)
