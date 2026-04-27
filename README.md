### Al Inayah

Interview assignement

### Installation

You can install this app by:
  1. bench get-app https://github.com/mohamed-afreen/Al-Inayah-Assignments.git
  2. bench --site "site_name" install-app al_inayah

### Testing

You can test this apps workflow by creating agencies, manufacturer, manufacturer items and its reports. these all things are accessible in Al inayah workspace.

### AI Usage Logs

AI prompts and solution will be accessible in the file "ai_usage_log.txt"

### API Testing

api: http://al-inayah.local:8000/api/method/al_inayah.manufacturer_item_mapping.api.get_manufacturer.get_manufacturer_mappings
params/body:
  {
    "item_code": "D-360"
  }
  
response:
  {
    "message": {
        "item_code": "D-360",
        "mappings": [
          {
                "manufacturers": "Neopharma",
                "item_code": "D-360",
                "part_number": "D-360",
                "gtin": null
            },
            {
                "manufacturers": "Globalpharma",
                "item_code": "D-360",
                "part_number": "ABC-123",
                "gtin": "3242"
            }
        ]
    }
}
