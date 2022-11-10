# 生成全流程任务

from matAgent.pso import PsoSwarm

def test_all_tasks_generate():
    # evaluate_optimizers = [ClpsoSwarm, FdrpsoSwarm, HpsotvacSwarm, LipsSwarm, PsoSwarm, ShpsoSwarm, HrlepsoBaseSwarm,
    #                        GwoSwarm]
    # base_evaluate_optimizers = [ClpsoSwarm, FdrpsoSwarm, HpsotvacSwarm, LipsSwarm, OlpsoSwarm, PsoSwarm, ShpsoSwarm,
    #                             EpsoSwarm, GwoSwarm]  # 都用一样的

    evaluate_optimizers = [PsoSwarm]
    base_evaluate_optimizers = [HpsotvacSwarm]  # 都用一样的
    runtimes = 1
    separate_trains = [False]
    groups = [5, ]
    train_max_episode = 1
    train_max_steps = 100 * train_max_episode
    dims = [20, ]
    evaluate_function = list(range(1, 2, 1))

    task = {'type': 'top',
            'evaluate_optimizers': evaluate_optimizers,
            'base_evaluate_optimizers': base_evaluate_optimizers,
            'evaluate_function': evaluate_function,
            'runtimes': runtimes,
            'separate_trains': separate_trains,
            'groups': groups,
            'train_max_episode': train_max_episode,
            'train_max_steps': train_max_steps,
            'dims': dims,
            'train_times': 2,
            'lr_critic': 1e-4,
            'lr_actor': 1e-6,
            }

    return [task]


def all_tasks_generate():
    evaluate_optimizers = [PsoSwarm]

    base_evaluate_optimizers = [PsoSwarm]  # 都用一样的
    runtimes = 10
    separate_trains = [False, True]
    # groups = [1, 3, 5, 7, 9]
    groups = [5]
    train_max_episode = 600
    train_max_steps = train_max_episode * 100
    dims = [30]
    evaluate_function = list(range(1, 29, 1))
    train_times = 1

    task = {'type': 'top',
            'evaluate_optimizers': evaluate_optimizers,
            'base_evaluate_optimizers': base_evaluate_optimizers,
            'evaluate_function': evaluate_function,
            'runtimes': runtimes,
            'separate_trains': separate_trains,
            'groups': groups,
            'train_max_episode': train_max_episode,
            'train_max_steps': train_max_steps,
            'dims': dims,
            'train_times': train_times,
            'lr_critic': 1e-4,
            'lr_actor': 1e-6,
            }

    return [task]






if __name__ == '__main__':
    test_all_tasks_generate()
