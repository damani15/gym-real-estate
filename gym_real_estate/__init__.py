from gym.envs.registration import register

register(
    id='gym-real-estate-v0',
    entry_point='gym_real-estate.envs:Real-EstateEnv',
)
