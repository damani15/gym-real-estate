from gym.envs.registration import register

register(
    id='realestate-v0',
    entry_point='gym_realestate.envs:RealestateEnv',
)
register(
    id='realestate-extrahard-v0',
    entry_point='gym_foo.envs:RealestateExtraHardEnv',
)