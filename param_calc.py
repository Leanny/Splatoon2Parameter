import json
from math import isclose, log2
import argparse

parameter = json.load(open("parameter.json"))

def get_parameter_list(main_name, sub_name, parameter):
    suffix = ["High", "Mid", "Low"]
    return [parameter[main_name][sub_name+'_'+s] for s in suffix]

abilities = {
    'Ink Saver Main - Low': get_parameter_list('MainInkSave', 'ConsumeRt_Main_Low', parameter),
    'Ink Saver Main - Mid': get_parameter_list('MainInkSave', 'ConsumeRt_Main', parameter),
    'Ink Saver Main - High': get_parameter_list('MainInkSave', 'ConsumeRt_Main_High', parameter),
    'Ink Saver Sub - Low': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub_Low', parameter),
    'Ink Saver Sub - Mid': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub', parameter),
    'Ink Saver Sub - High': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub_High', parameter),
    'Swim Speed - Heavy': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth_BigWeapon', parameter),
    'Swim Speed - Mid': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth', parameter),
    'Swim Speed - Light': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth_ShortWeapon', parameter),
    'Run Speed - Heavy': get_parameter_list('RunSpeedUp', 'MoveVel_Human_BigWeapon', parameter),
    'Run Speed - Mid': get_parameter_list('RunSpeedUp', 'MoveVel_Human', parameter),
    'Run Speed - Light': get_parameter_list('RunSpeedUp', 'MoveVel_Human_ShortWeapon', parameter),
    'Run Speed - Shooting': get_parameter_list('RunSpeedUp', 'MoveVelRt_Human_Shot', parameter),
    'Run Speed - Shooting, Splatling': get_parameter_list('RunSpeedUp', 'MoveVelRt_Human_ShotG', parameter),
    'Special Charge Up': get_parameter_list('SpecialIncreaseUp', 'SpecialRt_Charge', parameter),
    'Quick Respawn - Die Frames': get_parameter_list('RespawnTimeSave', 'Dying_AroudFrm', parameter),
    'Quick Respawn - Deathcam Frames': get_parameter_list('RespawnTimeSave', 'Dying_ChaseFrm', parameter),
    'Special Saver': get_parameter_list('RespawnSpecialGaugeSave', 'SpecialRt_Restart', parameter),
    'Special Saver - Splashdown': get_parameter_list('RespawnSpecialGaugeSave', 'SpecialRt_Restart_SuperLanding', parameter),
    'Ink Resistance - Jump(story)': get_parameter_list('OpInkEffectReduction', 'OpInk_JumpGnd_Msn', parameter),
    'Ink Resistance - Jump': get_parameter_list('OpInkEffectReduction', 'OpInk_JumpGnd', parameter),
    'Ink Resistance - Shoot K': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd_ShotK', parameter),
    'Ink Resistance - Shoot': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd_Shot', parameter),
    'Ink Resistance - Run': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd', parameter),
    'Ink Resistance - Dmg Limit': get_parameter_list('OpInkEffectReduction', 'OpInk_Damage_Lmt', parameter),
    'Ink Resistance - Dmg Per Frame': get_parameter_list('OpInkEffectReduction', 'OpInk_Damage', parameter),
    'Cold Blooded - Thermal Ink Time Reduction': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt_Thermal', parameter),
    'Cold Blooded - Silhouette Far': get_parameter_list('MarkingTimeReduction', 'Silhouette_DistFar', parameter),
    'Cold Blooded - Silhouette Close': get_parameter_list('MarkingTimeReduction', 'Silhouette_DistNear', parameter),
    'Cold Blooded - Ink Mine': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt_Trap', parameter),
    'Cold Blooded - Point Sensor': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt', parameter),
    'Quick Super Jump - Prepare': get_parameter_list('JumpTimeSave', 'DokanWarp_TameFrm', parameter),
    'Quick Super Jump - Jump': get_parameter_list('JumpTimeSave', 'DokanWarp_MoveFrm', parameter),
    'Ink Recovery Up - In Ink': get_parameter_list('InkRecoveryUp', 'RecoverFullFrm_Ink', parameter),
    'Ink Recovery Up - Standing': get_parameter_list('InkRecoveryUp', 'RecoverNrmlFrm_Ink', parameter),
    'Bomb Distance Up': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ', parameter),
    'Bomb Distance Up - Fizzy': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ_BombPiyo', parameter),
    'Bomb Distance Up - Point Sensor': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ_PointSensor', parameter),
    'Bomb Defense - Heavy Sub': get_parameter_list('BombDamageReduction', 'BurstDamageRt_SubH', parameter),
    'Bomb Defense - Heavy Light': get_parameter_list('BombDamageReduction', 'BurstDamageRt_SubL', parameter),
    'Bomb Defense - Special': get_parameter_list('BombDamageReduction', 'BurstDamageRt_Special', parameter),
    'Bomb Defense - Additional': get_parameter_list('BombDamageReduction', 'BurstDamageRt_Main', parameter),
    'Special Power Up - Baller HP': get_parameter_list('SpecialTime_Up', 'AquaBall_HP', parameter),
    'Special Power Up - Inkjet Bullet Damage Radius Multiplier': get_parameter_list('SpecialTime_Up', 'Inkjet_BombCoreRadiusRate', parameter),
    'Special Power Up - Inkjet Explosion Paint Radius': get_parameter_list('SpecialTime_Up', 'Inkjet_Burst_PaintR', parameter),
    'Special Power Up - Inkjet Explosion Paint Splash Radius': get_parameter_list('SpecialTime_Up', 'Inkjet_Burst_SplashPaintR', parameter),
    'Special Power Up - Inkjet Explosion Paint Splash Velocity H': get_parameter_list('SpecialTime_Up', 'Inkjet_Burst_SplashVelH', parameter),
    'Special Power Up - Inkjet Explosion Paint Splash Velocity L': get_parameter_list('SpecialTime_Up', 'Inkjet_Burst_SplashVelL', parameter),
    'Special Power Up - Ink Storm Duration': get_parameter_list('SpecialTime_Up', 'RainCloud_RainAreaFrame', parameter),
    'Special Power Up - Ink Armor Wind Up Time': get_parameter_list('SpecialTime_Up', 'SuperArmor_EnergyAbsorbFrm', parameter),    
    'Special Power Up - Ink Armor Object Shredder Multiplier': get_parameter_list('SpecialTime_Up', 'SuperArmor_ObjectEffect_Up_DamageRt', parameter),   
    'Special Power Up - Ink Armor Duration': get_parameter_list('SpecialTime_Up', 'SuperArmor_PaintGauge_SpecialFrm_DamageRt', parameter),   
    'Special Power Up - Booyah Ball Auto Charge Increase': get_parameter_list('SpecialTime_Up', 'SuperBall_ChargeRtAutoIncr', parameter),   
    'Special Power Up - Booyah Ball Object Shredder Multiplier': get_parameter_list('SpecialTime_Up', 'SuperBall_ObjectEffect_Up_DamageRt', parameter),   
    'Special Power Up - Bubble Blower Bubble Radius Multiplier': get_parameter_list('SpecialTime_Up', 'SuperBubble_BombCoreRadiusRate', parameter),
    'Special Power Up - Bubble Blower Burst Paint Radius': get_parameter_list('SpecialTime_Up', 'SuperBubble_Burst_PaintR', parameter),    
    'Special Power Up - Bubble Blower Maximum Collision Player Radius': get_parameter_list('SpecialTime_Up', 'SuperBubble_CollisionPlayerRadiusMax', parameter),   
    'Special Power Up - Bubble Blower Object Shredder Multiplier': get_parameter_list('SpecialTime_Up', 'SuperBubble_ObjectEffect_Up_DamageRt', parameter),   
    'Special Power Up - Splash Down Jump-In Additional Height': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Landing_AddHeight', parameter),    
    'Special Power Up - Splash Down Jump-In Additional Height (Stealth Jump)': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Landing_AddHeight_SJ', parameter),    
    'Special Power Up - Splash Down Jump-In Height': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Landing_Height', parameter),   
    'Special Power Up - Splash Down Jump-In Height (Stealth Jump)': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Landing_Height_SJ', parameter),   
    'Special Power Up - Splash Down Burst Radius Far': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Far', parameter),   
    'Special Power Up - Splash Down Burst Radius Far (Stealth Jump)': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Far_SJ', parameter),   
    'Special Power Up - Splash Down Burst Radius Middle': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Middle', parameter),   
    'Special Power Up - Splash Down Burst Radius Midle (Stealth Jump)': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Middle_SJ', parameter),   
    'Special Power Up - Splash Down Burst Radius Close': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Near', parameter),   
    'Special Power Up - Splash Down Burst Radius Close (Stealth Jump)': get_parameter_list('SpecialTime_Up', 'SuperLanding_Burst_Radius_Near_SJ', parameter), 
    'Special Power Up - Tenta Missiles Paint Radius': get_parameter_list('SpecialTime_Up', 'SuperMissiles_Burst_PaintR', parameter),    
    'Special Power Up - Tenta Missiles Cross Paint Radius': get_parameter_list('SpecialTime_Up', 'SuperMissiles_CrossPaintRadius', parameter),    
    'Special Power Up - Tenta Missiles Cross Paint Ray Length': get_parameter_list('SpecialTime_Up', 'SuperMissiles_CrossPaintRayLength', parameter),   
    'Special Power Up - Tenta Missiles Target Circle Radius': get_parameter_list('SpecialTime_Up', 'SuperMissiles_TargetInCircleRadius', parameter),   
    'Special Power Up - Sting Ray Duration': get_parameter_list('SpecialTime_Up', 'WaterCutter_PaintGauge_SpecialFrm', parameter)  
}

def calcSkillPoint2Percent(points):
    return min(max(0.0, 3.3*points-0.027*points**2), 100.0)
    
def lerpN(slope, percentage):
    if isclose(percentage, 0.0) or not slope >= 0.001:
        return 0.0
    return 1/percentage**(log2(slope))

def get_slope(ability):
    high, mid, low = ability
    if isclose(high, low):
        return 0.0
    return (mid-low)/(high-low)
    
def get_effect(ability, points, ninjasquid = False):
    high, mid, low = ability
    slope = get_slope(ability)
    tmp = calcSkillPoint2Percent(points)
    if ninjasquid:
        tmp *= 0.8 # ninja squid adds percentage penality
    percentage = tmp / 100.0
    result = low + (high - low) * lerpN(slope, percentage)
    if ninjasquid:
        return 0.9 * result # ninja squid reduces speed by 10%
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--ability', type=int)
    parser.add_argument('-n', '--ninja-squid', action='store_true')
    args = parser.parse_args()
    
    if args.ability is not None:
        names = sorted([*abilities.keys()])
        assert(args.ability>0 and args.ability<=len(names))
        
        name = names[args.ability-1]
        print(name)
        
        aps = sorted([mains*10 + subs*3 for mains in range(4-int(args.ninja_squid)) for subs in range(10)])
        
        print('{:<10}{:<}'.format('AP','Effect'))
        for ap in aps:
            effect = get_effect(abilities[name], ap, args.ninja_squid)
            print('{:<10}{:05.4f}'.format(str(ap).rjust(2), effect))
    else:
        print("""
                ____        _       _                      ____  
               / ___| _ __ | | __ _| |_ ___   ___  _ __   |___ \ 
               \___ \| '_ \| |/ _` | __/ _ \ / _ \| '_ \    __) |
                ___) | |_) | | (_| | || (_) | (_) | | | |  / __/ 
               |____/| .__/|_|\__,_|\__\___/ \___/|_| |_| |_____|
                     |_|                                         
                ____                                _            
               |  _ \ __ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ 
               | |_) / _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__|
               |  __/ (_| | | | (_| | | | | | |  __/ ||  __/ |   
               |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|   
                                                                 
        """)    
        
        names = sorted([*abilities.keys()])
        
        for i in range(0, len(names)-1,2):
            print('{:<76}{:<}'.format(str(i+1).rjust(2)+'. '+names[i], str(i+2).rjust(2)+'. '+names[i+1]))
        
        print()    
        parser.print_help()
                
