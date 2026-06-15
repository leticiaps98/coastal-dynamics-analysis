"""
Shoreline Dynamics Analysis (EPR & LRR)
Automated transect generation and shoreline change calculation using GeoPandas.
"""
import geopandas as gpd
from shapely.geometry import LineString
import pandas as pd
import numpy as np
from scipy.stats import linregress
import warnings
warnings.filterwarnings("ignore")

def generate_transects(baseline, spacing=50, length=2000):
    """Generates perpendicular transects along a coastal baseline."""
    transects = []
    length_base = baseline.length
    for dist in np.arange(0, length_base, spacing):
        pt = baseline.interpolate(dist)
        pt_next = baseline.interpolate(min(dist + 1, length_base))
        
        # Calculate angle perpendicular to the baseline
        angle = np.arctan2(pt_next.y - pt.y, pt_next.x - pt.x) + np.pi/2
        end_x = pt.x + length * np.cos(angle)
        end_y = pt.y + length * np.sin(angle)
        
        transects.append({'geometry': LineString([(pt.x, pt.y), (end_x, end_y)]), 'id': len(transects)})
    return gpd.GeoDataFrame(transects, crs=baseline.crs)

def calculate_epr(transects, shorelines, start_year, end_year):
    """Calculates the End Point Rate (EPR) between two shoreline positions."""
    g1, g2 = shorelines[start_year], shorelines[end_year]
    results = []
    for idx, row in transects.iterrows():
        t = row['geometry']
        i1, i2 = t.intersection(g1), t.intersection(g2)
        
        if not i1.is_empty and not i2.is_empty:
            p1 = i1 if i1.geom_type == 'Point' else i1.geoms[0]
            p2 = i2 if i2.geom_type == 'Point' else i2.geoms[0]
            
            # Distance difference divided by timespan (Positive = Accretion, Negative = Erosion)
            epr = (t.project(p1) - t.project(p2)) / (end_year - start_year)
            results.append({'id': row['id'], 'EPR_m_yr': epr})
            
    return pd.DataFrame(results)

def calculate_lrr(transects, shorelines, years_list):
    """Calculates the Linear Regression Rate (LRR) across multiple shorelines over time."""
    results = []
    for idx, row in transects.iterrows():
        t = row['geometry']
        distances, valid_years = [], []
        
        for year in years_list:
            if year in shorelines:
                intersection = t.intersection(shorelines[year])
                if not intersection.is_empty:
                    pt = intersection if intersection.geom_type == 'Point' else intersection.geoms[0]
                    distances.append(t.project(pt))
                    valid_years.append(year)
        
        # Linear regression requires at least 3 temporal points to be reliable
        if len(distances) >= 3:
            slope, intercept, r_val, p_val, std_err = linregress(valid_years, distances)
            results.append({
                'id': row['id'], 
                'LRR_m_yr': slope, 
                'R_squared': r_val**2
            })
            
    return pd.DataFrame(results)
