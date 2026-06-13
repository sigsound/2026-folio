#!/usr/bin/env python3
"""Downloads all project images from Webflow CDN into public/images/projects/[slug]/"""

import os
import subprocess

BASE_CDN = "https://cdn.prod.website-files.com/584096ac2d3763df78c00dd9/"
BASE_DIR = "/Users/nickwoods/Documents/sites/2026-folio/public/images/projects/"

def download(slug, local_name, cdn_filename):
    url = BASE_CDN + cdn_filename
    dest = os.path.join(BASE_DIR, slug, local_name)
    result = subprocess.run(
        ["curl", "-s", "-L", "-o", dest, url],
        capture_output=True
    )
    if result.returncode == 0 and os.path.getsize(dest) > 0:
        print(f"  ✓ {local_name}")
    else:
        print(f"  ✗ {local_name} — curl exit {result.returncode} ({url})")

PROJECTS = {
    "unified-experience": {
        "thumb":    ("thumb.jpg",        "6953008223a248a07c21af69_Unified%20Experience.jpg"),
        "hero":     ("hero.jpg",         "695300c3125c83ae70358498_UE%20-%20Product%20Silos.jpg"),
        "hisImage": ("his-image.jpg",    "69530a182505f0dae2e82e22_UE%20-%20Customer%20Pain%20Point.jpg"),
        "media": [
            ("media-1.jpg", "69530e83c171a846d9cd0d73_UE%20-%20Solution%201.jpg"),
            ("media-2.jpg", "695310935b7c5e3a2c5936f0_Two%20Apps%20to%20One.jpg"),
            ("media-3.jpg", "69531f947f8431ef69384940_UE%20-%20Customer%20Reactions.jpg"),
        ]
    },
    "matterport-3d-tools": {
        "thumb":    ("thumb.jpg",        "61e9f31434e6d5065c430d8f_Thumbnail.jpg"),
        "hero":     ("hero.jpg",         "61ea0bc596d2bf49ee1fc2fe_Thumbnail.jpg"),
        "hisImage": ("his-image.jpg",    "61e9f5119da56619b071b08b_Measurement.jpg"),
        "media": [
            ("media-1.jpg", "61e9f802ee1ea7b04f1111fd_Notes.jpg"),
            ("media-2.jpg", "61ea0bdaecb2e56f4e482021_Trim.jpg"),
            ("media-3.jpg", "61ea1674d5a24b7ce9cfce1e_Manual%20Blur.jpg"),
        ]
    },
    "quickbooks-connect-emerging-tech-showcase": {
        "thumb":    ("thumb.png",        "5c0c5bbb97f1294a0b5b3e1b_Screen%20Shot%202018-12-08%20at%204.01.52%20PM.png"),
        "hero":     ("hero.jpg",         "5c0c5a67a90b66c38b878723_qbc_01.jpg"),
        "hisImage": ("his-image.jpg",    "5c0c53cca90b6664dd8783d1_qbc_02.jpg"),
        "media": [
            ("media-1.jpg", "5c0c53dfdff7c45ef162d732_Bizloc%203.jpg"),
            ("media-2.jpg", "5c0c5730583e2f3de2ab3ccd_Bizloc.jpg"),
            ("media-3.jpg", "5c0c5a738da8f04dd4f9285d_Bizloc%20mobile.jpg"),
        ]
    },
    "nike-training-app": {
        "thumb":    ("thumb.jpg",        "5c0c478736137d2851dc2867_NTC_DT_P3_US.jpg"),
        "hero":     ("hero.jpg",         "5c0c471536137d34a6dc2846_Nike%20Screens%201.jpg"),
        "media": [
            ("media-1.jpg", "5c0c490136137d2464dc2905_Nike%20Screens%202.jpg"),
        ]
    },
    "design-futures": {
        "thumb":    ("thumb.jpg",        "5c0c2e07dff7c4faac62b0f3_Rectangle%20Copy%402x.jpg"),
        "hero":     ("hero.png",         "5c0c352cdff7c4247862b93b_Primary%20Brand%20Copy.png"),
        "hisImage": ("his-image.jpg",    "5c0c439697f1297aa15b1e21_DF%20Site.jpg"),
        "media": [
            ("media-1.jpg", "5c0c43c697f129054d5b1e40_DF%20Posters.jpg"),
            ("media-2.jpg", "5c0c43e3a90b6646bf877208_DF%20Team.jpg"),
        ]
    },
    "the-point": {
        "thumb":    ("thumb.jpg",        "589ad2d6a2c59c663da788eb_About_ThePoint.jpg"),
        "hero":     ("hero.jpg",         "589ad301dbf0b97f5096af1b_thepoint%20Home.jpg"),
        "hisImage": ("his-image.jpg",    "589ad306a2c59c663da788fe_thepoint%20List.jpg"),
        "media": [
            ("media-1.jpg", "589ad30a047ae8e564b5669a_thepoint%20Article.jpg"),
        ]
    },
    "demo-reel": {
        "thumb":    ("thumb.gif",        "592f053a46b03322be202e56_ossic.gif"),
        "hero":     ("hero.gif",         "592f053a46b03322be202e56_ossic.gif"),
    },
    "qualcomm-snapdragon": {
        "thumb":    ("thumb.jpg",        "589a5eea04380bf8074f30fc_thumb.jpg"),
        "hero":     ("hero.jpg",         "589a59dd866615ba07f33e4d_Qualcomm%20Snapdragon.jpg"),
        "hisImage": ("his-image.jpg",    "589a59e141f1f8c70b90c25f_QC%202.jpg"),
        "media": [
            ("media-1.jpg", "589a59e504380bf8074f2e1e_QC%203.jpg"),
            ("media-2.jpg", "589a59e8200c2d933b1f3410_QC%204.jpg"),
            ("media-3.jpg", "589a59ed200c2d933b1f341e_Wireframe.jpg"),
        ]
    },
    "oz-nashville": {
        "thumb":    ("thumb.jpg",        "58997be315fe7ce241e6e384_glass.jpg"),
        "hero":     ("hero.jpg",         "589acb206dc290a6649e7452_oz%20home.jpg"),
        "hisImage": ("his-image.jpg",    "58997c0450480cd959d30756_marquis_mock.jpg"),
        "media": [
            ("media-1.jpg", "589acb32d5513f1841f43cc7_oz%20venues%20one.jpg"),
            ("media-2.jpg", "589acb409c395ee568b5be45_oz%20about.jpg"),
            ("media-3.jpg", "589acb46d5513f1841f43cde_oz%20program.jpg"),
        ]
    },
    "identities": {
        "thumb":    ("thumb.jpg",        "589a609041f1f8c70b90c5c6_brands%20thumb.jpg"),
        "hero":     ("hero.jpg",         "589a69a4725c1cbb45166caa_Brainxchange.jpg"),
        "hisImage": ("his-image.jpg",    "589b8bec1f394ea53d071e55_Logo%20BX%402x-80.jpg"),
        "media": [
            ("media-1.jpg", "589a69b37818a7be3145bdee_Billups.jpg"),
            ("media-2.jpg", "589a708c047ae8e564b54a30_techpop.jpg"),
            ("media-3.jpg", "589b8e0b2e2496fa40359314_holling.jpg"),
        ]
    },
    "captured-52": {
        "thumb":    ("thumb.jpg",        "5896d7d6176071a2715c5cd0_emboss.jpg"),
        "hero":     ("hero.jpg",         "58990be0adc2755534a86305_Captured%2052.jpg"),
        "hisImage": ("his-image.jpg",    "5896d7238fe5ff7f71fec9d7_c52_wordmark.jpg"),
        "media": [
            ("media-1.jpg", "5896d7502a2594502197edcf_Z31A5059_1728.jpg"),
            ("media-2.jpg", "589bca5026e3bc615f48885c_poster_black3.jpg"),
        ]
    },
    "mideast-youth": {
        "thumb":    ("thumb.jpg",        "58865b2c65f4e8235f107c6f_gaza_genocide-p-1600x900.jpeg"),
        "hero":     ("hero.jpg",         "589ad62ed5513f1841f442f5_cover.jpg"),
    },
    "adidas-recovery": {
        "thumb":    ("thumb.jpg",        "587836803a5af1887955e947_adicomp_o.jpg"),
        "hero":     ("hero.jpg",         "58997ddd7f55043c07cf38b8_adidas_recovery.jpg"),
        "hisImage": ("his-image.jpg",    "58783687880216990135adf1_mens2.jpg"),
        "media": [
            ("media-1.jpg", "5878369e27847d66511b6a3d_mensrecovery.jpg"),
            ("media-2.png", "589adb4b2e2496fa403521eb_recovery1.png"),
        ]
    },
    "the-prids": {
        "thumb":    ("thumb.jpg",        "592f06754d51ec621f3528e5_spin.jpg"),
        "hero":     ("hero.jpg",         "589ba726d5513f1841f49a0f_Cover_RGB_tan_long.jpg"),
        "hisImage": ("his-image.jpg",    "58782cf7296f825008687a0c_prids_024.jpg"),
        "media": [
            ("media-1.jpg", "589ba85fb3ce13a250242d9d_wmte_allup.jpg"),
            ("media-2.jpg", "589ba5edba3a1f0369f8b43e_helio%20poster.jpg"),
            ("media-3.jpg", "589baa1b6dc290a6649edab7_prids_021.jpg"),
        ]
    },
    "holiday-survival-guide": {
        "thumb":    ("thumb.jpg",        "58644ecf844ff847297312a4_airplane_004.jpg"),
        "hero":     ("hero.jpg",         "5898d25dbbccb1ff2bf36a42_HGG%20Primary.jpg"),
        "hisImage": ("his-image.jpg",    "588e9450528d21b745647cbc_office_000.jpg"),
        "media": [
            ("media-1.jpg", "588e94666c5d8fdd05632609_airplane.jpg"),
            ("media-2.jpg", "5898d260f29bebaa63a177c0_HGG%20Responsive.jpg"),
            ("media-3.jpg", "589ada76d90fbc9f3bf701d8_HGG%20onsite.jpg"),
        ]
    },
    "digital-trends": {
        "thumb":    ("thumb.jpg",        "58782b857d0ac9f16f239eb5_DT%20Mobile.jpg"),
        "hero":     ("hero.jpg",         "5898faecf29bebaa63a19a58_Loading%20Screen.jpg"),
        "hisImage": ("his-image.jpg",    "589901ef5bfda235219fec19_On%20Hover.jpg"),
        "media": [
            ("media-1.jpg", "589906a2176071a2715da1cc_DT%20Topic%20Hubs.jpg"),
            ("media-2.jpg", "58990b05f29bebaa63a1a321_DT%20Video%20Player.jpg"),
        ]
    },
}

for slug, images in PROJECTS.items():
    dir_path = os.path.join(BASE_DIR, slug)
    os.makedirs(dir_path, exist_ok=True)
    print(f"\n{slug}/")
    for key, value in images.items():
        if key == "media":
            for local_name, cdn_filename in value:
                download(slug, local_name, cdn_filename)
        else:
            local_name, cdn_filename = value
            download(slug, local_name, cdn_filename)

print("\nDone.")
