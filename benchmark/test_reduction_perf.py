import torch

from .performance_utils import (
    BLAS_BATCH,
    FLOAT_DTYPES,
    INT_DTYPES,
    REDUCTION_BATCH,
    SIZES,
    Benchmark,
    unary_arg,
)


def test_perf_all():
    bench = Benchmark(
        op_name="all",
        torch_op=torch.all,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_amax():
    bench = Benchmark(
        op_name="amax",
        torch_op=torch.amax,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_any():
    bench = Benchmark(
        op_name="any",
        torch_op=torch.any,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_argmax():
    bench = Benchmark(
        op_name="argmax",
        torch_op=torch.argmax,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_cross_entropy_loss():
    def cross_entropy_loss_args(dtype, batch, size):
        inp = torch.randn([batch, size], dtype=dtype, device="cuda")
        target = torch.randint(
            0,
            size,
            [
                batch,
            ],
            device="cuda",
        )
        return inp, target

    bench = Benchmark(
        op_name="CrossEntropyLoss",
        torch_op=torch.nn.CrossEntropyLoss(),
        arg_func=cross_entropy_loss_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_cumsum():
    def cumsum_args(dtype, batch, size):
        inp = torch.randn([batch, size], dtype=dtype, device="cuda")
        return inp, 1

    bench = Benchmark(
        op_name="cumsum",
        torch_op=torch.cumsum,
        arg_func=cumsum_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_nonzero():
    def nonzero_args(dtype, batch, size):
        if dtype == torch.bool:
            inp = torch.randint(0, 2, [batch, size], dtype=torch.int, device="cuda").to(
                torch.bool
            )
        else:
            inp = torch.randint(0, 2, [batch, size], dtype=dtype, device="cuda")
        return (inp,)

    bench = Benchmark(
        op_name="nonzero",
        torch_op=torch.nonzero,
        arg_func=nonzero_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_nonzero_int():
    def nonzero_args(dtype, batch, size):
        if dtype == torch.bool:
            inp = torch.randint(0, 2, [batch, size], dtype=torch.int, device="cuda").to(
                torch.bool
            )
        else:
            inp = torch.randint(0, 2, [batch, size], dtype=dtype, device="cuda")
        return (inp,)

    bench = Benchmark(
        op_name="nonzero_int",
        torch_op=torch.nonzero,
        arg_func=nonzero_args,
        dtypes=INT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_groupnorm():
    def group_norm_args(dtype, batch, size):
        C = 16
        G = 16
        inp = torch.randn([batch, C, size], dtype=dtype, device="cuda")
        weight = torch.randn(
            [
                C,
            ],
            dtype=dtype,
            device="cuda",
        )
        bias = torch.randn(
            [
                C,
            ],
            dtype=dtype,
            device="cuda",
        )
        return inp, G, weight, bias

    bench = Benchmark(
        op_name="groupnorm",
        torch_op=torch.nn.functional.group_norm,
        arg_func=group_norm_args,
        dtypes=FLOAT_DTYPES,
        batch=BLAS_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_layernorm():
    def layer_norm_args(dtype, batch, size):
        inp = torch.randn([batch, size], dtype=dtype, device="cuda")
        weight = torch.randn(
            [
                size,
            ],
            dtype=dtype,
            device="cuda",
        )
        bias = torch.randn(
            [
                size,
            ],
            dtype=dtype,
            device="cuda",
        )
        return (
            inp,
            [
                size,
            ],
            weight,
            bias,
        )

    bench = Benchmark(
        op_name="layernorm",
        torch_op=torch.layer_norm,
        arg_func=layer_norm_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_weightnorm_interface():
    def weight_norm_args(dtype, batch, size):
        v = torch.randn([batch, size], dtype=dtype, device="cuda")
        g = torch.randn([batch], dtype=dtype, device="cuda")
        return v, g, 0

    bench = Benchmark(
        op_name="weight_norm_interface",
        torch_op=torch._weight_norm_interface,
        arg_func=weight_norm_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_weightnorm():
    def weight_norm_args(dtype, batch, size):
        v = torch.randn([batch, size], dtype=dtype, device="cuda")
        g = torch.randn([batch, size], dtype=dtype, device="cuda")
        return v, g, 0

    bench = Benchmark(
        op_name="weight_norm",
        torch_op=torch._weight_norm,
        arg_func=weight_norm_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_log_softmax():
    bench = Benchmark(
        op_name="log_softmax",
        torch_op=torch.nn.functional.log_softmax,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_max():
    bench = Benchmark(
        op_name="max",
        torch_op=torch.max,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_mean():
    bench = Benchmark(
        op_name="mean",
        torch_op=torch.mean,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_min():
    bench = Benchmark(
        op_name="min",
        torch_op=torch.min,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_prod():
    bench = Benchmark(
        op_name="prod",
        torch_op=torch.prod,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_softmax():
    bench = Benchmark(
        op_name="softmax",
        torch_op=torch.nn.functional.softmax,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_softmax_backward():
    bench = Benchmark(
        op_name="softmax",
        torch_op=torch.nn.functional.softmax,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
        is_backward=True,
    )
    bench.run()


def test_perf_sum():
    bench = Benchmark(
        op_name="sum",
        torch_op=torch.sum,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_var_mean():
    bench = Benchmark(
        op_name="var_mean",
        torch_op=torch.var_mean,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_vector_norm():
    bench = Benchmark(
        op_name="vector_norm",
        torch_op=torch.linalg.vector_norm,
        arg_func=unary_arg,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_index_select():
    def index_select_args(dtype, batch, size):
        inp = torch.randn([batch, size], dtype=dtype, device="cuda")

        threshold = 0.1
        dim = 0
        index_size = inp.size(dim)
        from math import floor

        index = torch.randint(
            0, index_size, [floor(index_size * threshold)], device="cuda"
        )
        return (inp, dim, index)

    bench = Benchmark(
        op_name="index_select",
        torch_op=torch.index_select,
        arg_func=index_select_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_masked_select():
    def masked_select_args(dtype, batch, size):
        inp = torch.randn([batch, size], dtype=dtype, device="cuda")
        mask = torch.randn([batch, size], dtype=dtype, device="cuda") < 0.3
        return (inp, mask)

    bench = Benchmark(
        op_name="masked_select",
        torch_op=torch.masked_select,
        arg_func=masked_select_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_scatter():
    def scatter_args(dtype, batch, size):
        inp_shape = [batch, size]
        src_shape = [batch // 16, size // 16]
        inp = torch.randn(inp_shape, dtype=dtype, device="cuda")
        src = torch.randn(src_shape, dtype=dtype, device="cuda")
        import random

        dim = random.choice([0, 1])
        size_dim = min(src_shape[dim], inp_shape[dim])

        index_shape = [
            random.randint(1, min(src_shape[0], inp_shape[0])),
            random.randint(1, min(src_shape[1], inp_shape[1])),
        ]
        index = torch.empty(tuple(index_shape), dtype=torch.long, device="cuda")

        m, n = index_shape

        index_size_dim = index_shape[dim]
        # make unique indices
        for i in range(1 if dim == 0 else m):
            for j in range(1 if dim == 1 else n):
                ii = [i, j]
                ii[dim] = slice(0, index.size(dim) + 1)
                index[tuple(ii)] = torch.randperm(size_dim)[0:index_size_dim]

        return (inp, dim, index, src)

    bench = Benchmark(
        op_name="scatter",
        torch_op=torch.scatter,
        arg_func=scatter_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_perf_gather():
    def gather_args(dtype, batch, size):
        inp_shape = [batch, size]
        inp = torch.randn(inp_shape, dtype=dtype, device="cuda")
        import random

        dim = random.choice([0, 1])
        size_dim = inp_shape[dim]
        index_shape = [
            random.randint(1, inp_shape[0]),
            random.randint(1, inp_shape[1]),
        ]
        index = torch.empty(tuple(index_shape), dtype=torch.long, device="cuda")

        m, n = index_shape

        index_size_dim = index_shape[dim]
        # make unique indices
        for i in range(1 if dim == 0 else m):
            for j in range(1 if dim == 1 else n):
                ii = [i, j]
                ii[dim] = slice(0, index.size(dim) + 1)
                index[tuple(ii)] = torch.randperm(size_dim)[0:index_size_dim]

        return (inp, dim, index)

    bench = Benchmark(
        op_name="gather",
        torch_op=torch.gather,
        arg_func=gather_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_slice_scatter_perf():
    def slice_scatter_args(dtype, batch, size):
        shape = [batch, size]
        import random

        dim = random.choice([0, 1])
        start = 16
        end = 1024
        step = 2

        inp = torch.randn(shape, dtype=dtype, device="cuda")

        range = end - start
        valid_shape = list(inp.shape)
        if end < start:
            range = 0
        elif (end - start) > valid_shape[dim]:
            range = valid_shape[dim]
            start = 0
            end = valid_shape[dim]

        valid_shape[dim] = (range + (step - 1)) // step
        src = torch.randn(valid_shape, dtype=dtype, device="cuda")
        return (inp, src, dim, start, end, step)

    bench = Benchmark(
        op_name="slice_scatter",
        torch_op=torch.slice_scatter,
        arg_func=slice_scatter_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()


def test_select_scatter_perf():
    def select_scatter_args(dtype, batch, size):
        shape = [batch, size]
        import random

        dim = random.choice([0, 1])

        import random

        index = random.randint(0, shape[dim] - 1)
        inp = torch.randn(shape, dtype=dtype, device="cuda")

        src_shape = list(inp.shape)
        del src_shape[dim]
        src = torch.randn(src_shape, dtype=dtype, device="cuda")

        return (inp, src, dim, index)

    bench = Benchmark(
        op_name="select_scatter",
        torch_op=torch.select_scatter,
        arg_func=select_scatter_args,
        dtypes=FLOAT_DTYPES,
        batch=REDUCTION_BATCH,
        sizes=SIZES,
    )
    bench.run()
