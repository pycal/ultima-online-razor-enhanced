Player.UseSkill('Poisoning')
Misc.Pause(600)
poison_pot = Items.FindByID(0x0F0A, -1, -1)
wep = Items.FindByID(0x1401, -1, -1)
Target.TargetExecute(poison_pot)
Misc.Pause(600)
Target.TargetExecute(wep)