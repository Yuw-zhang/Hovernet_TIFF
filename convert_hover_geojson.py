import uuid
from typing import List
import json

# Type mapping for QuPath-style annotation
TYPE_NUCLEI_DICT = {
    1: "Neoplastic",
    2: "Inflammatory",
    3: "Connective",
    4: "Dead",
    5: "Epithelial"
}

COLOR_DICT = {
    1: [255, 0, 0],
    2: [0, 255, 0],
    3: [0, 0, 255],
    4: [255, 255, 0],
    5: [255, 0, 255]
}


def get_template_segmentation():
    return {
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": []},
        "properties": {
            "classification": {"name": "", "color": []},
            "isLocked": False
        },
        "id": ""
    }


def get_template_point():
    return {
        "type": "Feature",
        "geometry": {"type": "MultiPoint", "coordinates": []},
        "properties": {
            "classification": {"name": "", "color": []},
            "isLocked": False
        },
        "id": ""
    }


def convert_hovernet_to_geojson(json_data, polygons=True) -> List[dict]:
    nuc_dict = json_data["nuc"]
    geojson_features = []

    for _, cell in nuc_dict.items():
        cell_type = cell["type"]
        classification_name = TYPE_NUCLEI_DICT.get(cell_type, f"Type_{cell_type}")
        classification_color = COLOR_DICT.get(cell_type, [128, 128, 128])

        if polygons:
            contour = cell["contour"]
            if contour[0] != contour[-1]:
                contour.append(contour[0])  # Close polygon
            feature = get_template_segmentation()
            feature["geometry"]["coordinates"] = [contour]
        else:
            centroid = cell["centroid"]
            feature = get_template_point()
            feature["geometry"]["coordinates"] = [centroid]

        feature["id"] = str(uuid.uuid4())
        feature["properties"]["classification"]["name"] = classification_name
        feature["properties"]["classification"]["color"] = classification_color

        geojson_features.append(feature)

    return geojson_features


# Example usage:
if __name__ == "__main__":
    with open("M023_US16/hovernet_output/Image_02_M023_40X_C24.json") as f:
        hovernet_json = json.load(f)

    geojson_obj = {
        "type": "FeatureCollection",
        "features": convert_hovernet_to_geojson(hovernet_json, polygons=True)  # or False for centroids
    }

    with open("hovernet_C24.geojson", "w") as f:
        json.dump(geojson_obj, f, indent=2)

