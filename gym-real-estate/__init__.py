from gym.envs.registration import register

register(
    id='gym-real-estate-v0',
    entry_point='gym-real-estate.envs:RealEstateEnv',
)
