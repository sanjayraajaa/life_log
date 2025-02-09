f_config = [
    {
        "doctype": "Role",
        "filters": [
            ["name", "in", ["Life Log User", "Life Log Admin"]]
        ]
    },
    {
        "doctype": "Workspace",
        "filters": [
            ["name", "in", ["Life Log"]]
        ]
    }
]