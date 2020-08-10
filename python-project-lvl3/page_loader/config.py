default_output_dir = "./page_loader_source"
logging = {
    "available_list": ["error", "info", "debug"],
    "default": "error",
}
tests = {
    "directory": "./tests/result"
}
convert_url_to_filename = {
    "delemiter": "_",
}
source_tags = [
    {"name": "img", "attr": "src"},
    {"name": "link", "attr": "href"},
    {"name": "script", "attr": "src"},
]
