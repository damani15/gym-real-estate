from gym.envs.registration import register

register(
    id='real_estate-v0',
    entry_point='gym_real_estate.envs:RealEstateEnv',
)

