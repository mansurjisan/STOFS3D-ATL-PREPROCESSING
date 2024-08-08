# STOFS3D-ATL-PREPROCESSING

# STOFS 3D ATL Script Hierarchy Table

| Main Script | Scripts Called | Purpose |
|-------------|----------------|---------|
| jstofs_3d_atl_prep.ecf | 1. JSTOFS_3D_ATL_PREP | Main job script |
| JSTOFS_3D_ATL_PREP | 1. exstofs_3d_atl_prep_processing.sh | Main processing script |
|  | 2. setpdy.sh | Sets up date variables |
|  | (Other scripts may be called, need to check script contents) | |
| exstofs_3d_atl_prep_processing.sh | 1. stofs_3d_atl_create_param_nml.sh | Creates param.nml file |
|  | 2. stofs_3d_atl_create_bctides_in.sh | Creates bctides.in file |
|  | 3. stofs_3d_atl_create_river_forcing_nwm.sh | Creates river forcing from NWM |
|  | 4. stofs_3d_atl_create_surface_forcing_gfs.sh | Creates surface forcing from GFS |
|  | 5. stofs_3d_atl_create_surface_forcing_hrrr.sh | Creates surface forcing from HRRR |
|  | 6. stofs_3d_atl_create_obc_3dth_nudge.sh | Creates OBC 3DTH nudging |
|  | (Other scripts may be called, need to check script contents) | |

## Main Flow

https://mermaid.live/view#pako:eNqFkl1r2zAUhv-KUGBXjmtHju3oYtDGCWwMGpaMwuJhVPso0apIRpLXZGn--5Q2A0NGJxA6L5znPR_oiGvdAKaYS_1cb5lxaFWUqlS1ZNYWwJGtjWjd9CwRF1LSwbjJGcsD64x-AjoghFzi4bNo3JaO2n1Qa6kNHXDOe1at0TVY2_ea5Pxx8r5Xz8Az0Kc5Z1HG_kOXCvlzuy7xT-s0txVpKuZk1RpoQ6h5iX9QSvtjDocfX6ZMSvuC7jz2ebm6ny8rUlS3qy_V4utscYW81bjrk1NPwv6qYnVZglCb0G7_YXRp99VqCc47FetPSjjBJJqpX8JotQPlzlx_n_0O_KqEAk_OPNl27ua-c_5BhTBQO20E2PfwhW-TmTM_Xz9o82RbVsM18IYU6AOa-TtHw9Cz3yw06PHgxy8VDvAOzI6Jxv-v4zm9xG4LOygx9WEDnHXSlbhUJ5_KOqeXB1Vj6kwHATa622wx5Uxar7q2YQ4KwTaG7f6mtEx917ovMT3iPabJZBLmUUaSNJ-MSBaTAB8wjUkSknGap9loRNKIxKcA_37lozCNkyxOkyhLoigbJ-T0B0KfB8Y


## Initial Environment

https://mermaid.live/view#pako:eNqFk8tu2zAQRX-FoLdyoIdliVx0UauLFglaNEEL1OpiLA0lIhQpUGQT1_C_h3bTQotC4WoGuOfOA5wTbUyLlFOhzFPTg3Xkoap1rRsF01ShIFNj5eh2l5QIqRRf5W0JUEaTs-YR-SrLstd4_SRb1_N0fI4ao4zlKyHEzGq0psFpmnuxUhzYstfMIDA4p4WAuIA36FqT8Kr9Ry2dBEU-6F_SGj2gdj855_OmXqVkvX5HqmR_a6Ald6b1CqdFabq_R0fewyQb8g2shMNbRLbfWQSH5Luxj1J3pJIWG2fscRHbXAr5kXwyB3Jrui6Qi_r82thn70bvyM7osBy1CGz3QSVk5y2SBzkgCbwLVZanKa5l_o1AvoDrl4nySoTdoiJfvQ6EhQEd2v9gNKID2gFkG_7p6WJTU9fjgDXlIWxRgFeuprU-Byl4Z-6PuqHcWY8RtcZ3PeUC1BQyP7Zh65WELtT7KxlB_zBmnlJ-os-Ul_FNzIptxoqM5VmcpBE9Up7F2U0ex8mGJemWlZvyHNHfVz4J8nyTFqxkLGdFsi0jiq0MO7n7c2XXYzu_AA0pIxw

# Pre-processing

https://mermaid.live/view#pako:eNqFkk2PmzAQhv-KNbkSlPARjA89NFE2_ZbIngpV5DXjgAoY2aabbTb_fZ0qW6G2Kj7NSM_zeizPGYQqERjIRj2KimtL7jdFV3Si4cZsUBIjdN3b9bUlsm4aNotLyjn1jNXqO7JZGIa3ev5Yl7ZiQX_yhGqUZjMp5Siq10qgMeOslMqH9P9ZowDn4NiWki8SPmEXHXFnnReAJ2OVNIewPHDbHHqN_eE2U90dfVMV8I0xNnrxzSXz-ZvntUZu0TyTu7znmrd-1zZX_PdQ_4R3-YOwdYnGr7tp-l2e1T9Qk63Swo00LbzP94OWXOCrQu62-2ntw1_aLsuyae9j_uXtmoSb-x35PJRHnDY-5Rkae92rreP-4MGDFnXL69Jt4PnqF2ArbLEA5soSJR8aW0DRXRzKB6v2T50AZvWAHmg1HCtgkjfGdUNfuhs3NT-6v3lFet59VWrcAjvDCVji08UyoWlMY5qu4njpwROwIIz81SpOwyBMIkqDJLp48PNXwNJfLKMojcMkSJIgWK7o5QW1ahG-
