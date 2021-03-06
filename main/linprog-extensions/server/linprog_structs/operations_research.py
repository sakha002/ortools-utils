# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: operations_research/optional_boolean.proto, operations_research/linear_solver.proto, operations_research/linear_extension.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


class OptionalBoolean(betterproto.Enum):
    """
    A "three-way" boolean: unspecified, false or true. We don't use the value
    of 1 to increase the chance to catch bugs: eg. in python, a user may set a
    proto field of this type enum to a boolean value without type checks, if
    they set it to True, the proto validity code will catch it (because it'll
    be cast to 1, which is an invalid enum value). Note that if the user sets
    if to False (i.e. 0), it will be caught by the routing library's parameter
    validity check too.
    """

    BOOL_UNSPECIFIED = 0
    BOOL_FALSE = 2
    BOOL_TRUE = 3


class MPSolverResponseStatus(betterproto.Enum):
    """
    Status returned by the solver. They follow a hierarchical nomenclature, to
    allow us to add more enum values in the future. Clients should use
    InCategory() to match these enums, with the following C++ pseudo-code: bool
    InCategory(MPSolverResponseStatus status, MPSolverResponseStatus cat) {
    if (cat == MPSOLVER_OPTIMAL) return status == MPSOLVER_OPTIMAL;   while
    (status > cat) status >>= 4;   return status == cat; }
    """

    # The solver found the proven optimal solution. This is what should be
    # returned in most cases. WARNING: for historical reason, the value is zero,
    # which means that this value can't have any subcategories.
    MPSOLVER_OPTIMAL = 0
    # The solver had enough time to find some solution that satisfies all
    # constraints, but it did not prove optimality (which means it may or may not
    # have reached the optimal). This can happen for large LP models (Linear
    # Programming), and is a frequent response for time-limited MIPs (Mixed
    # Integer Programming). In the MIP case, the difference between the solution
    # 'objective_value' and 'best_objective_bound' fields of the
    # MPSolutionResponse will give an indication of how far this solution is from
    # the optimal one.
    MPSOLVER_FEASIBLE = 1
    # The model does not have any solution, according to the solver (which
    # "proved" it, with the caveat that numerical proofs aren't actual proofs),
    # or based on trivial considerations (eg. a variable whose lower bound is
    # strictly greater than its upper bound).
    MPSOLVER_INFEASIBLE = 2
    # There exist solutions that make the magnitude of the objective value as
    # large as wanted (i.e. -infinity (resp. +infinity) for a minimization (resp.
    # maximization) problem.
    MPSOLVER_UNBOUNDED = 3
    # An error (most probably numerical) occurred. One likely cause for such
    # errors is a large numerical range among variable coefficients (eg. 1e-16,
    # 1e20), in which case one should try to shrink it.
    MPSOLVER_ABNORMAL = 4
    # The solver did not have a chance to diagnose the model in one of the
    # categories above.
    MPSOLVER_NOT_SOLVED = 6
    # Like "NOT_SOLVED", but typically used by model validation functions
    # returning a "model status", to enhance readability of the client code.
    MPSOLVER_MODEL_IS_VALID = 97
    # Special value: the solver status could not be properly translated and is
    # unknown.
    MPSOLVER_UNKNOWN_STATUS = 99
    # Model errors. These are always deterministic and repeatable. They should be
    # accompanied with a string description of the error.
    MPSOLVER_MODEL_INVALID = 5
    # Something is wrong with the fields "solution_hint_var_index" and/or
    # "solution_hint_var_value".
    MPSOLVER_MODEL_INVALID_SOLUTION_HINT = 84
    # Something is wrong with the solver_specific_parameters request field.
    MPSOLVER_MODEL_INVALID_SOLVER_PARAMETERS = 85
    # Implementation error: the requested solver implementation is not available
    # (see MPModelRequest.solver_type). The linear solver binary was probably not
    # linked with the required library, eg
    # //ortools/linear_solver:linear_solver_scip for SCIP.
    MPSOLVER_SOLVER_TYPE_UNAVAILABLE = 7


class MPSosConstraintType(betterproto.Enum):
    SOS1_DEFAULT = 0
    SOS2 = 1


class MPSolverCommonParametersLPAlgorithmValues(betterproto.Enum):
    LP_ALGO_UNSPECIFIED = 0
    LP_ALGO_DUAL = 1
    LP_ALGO_PRIMAL = 2
    LP_ALGO_BARRIER = 3


class MPModelRequestSolverType(betterproto.Enum):
    GLOP_LINEAR_PROGRAMMING = 2
    CLP_LINEAR_PROGRAMMING = 0
    GLPK_LINEAR_PROGRAMMING = 1
    GUROBI_LINEAR_PROGRAMMING = 6
    XPRESS_LINEAR_PROGRAMMING = 101
    CPLEX_LINEAR_PROGRAMMING = 10
    SCIP_MIXED_INTEGER_PROGRAMMING = 3
    GLPK_MIXED_INTEGER_PROGRAMMING = 4
    CBC_MIXED_INTEGER_PROGRAMMING = 5
    GUROBI_MIXED_INTEGER_PROGRAMMING = 7
    XPRESS_MIXED_INTEGER_PROGRAMMING = 102
    CPLEX_MIXED_INTEGER_PROGRAMMING = 11
    BOP_INTEGER_PROGRAMMING = 12
    SAT_INTEGER_PROGRAMMING = 14
    KNAPSACK_MIXED_INTEGER_PROGRAMMING = 13


@dataclass
class MPVariableProto(betterproto.Message):
    """
    A variable is always constrained in the form:    lower_bound <= x <=
    upper_bound where lower_bound and upper_bound: - Can form a singleton: x =
    constant = lower_bound = upper_bound. - Can form a finite interval:
    lower_bound <= x <= upper_bound. (x is boxed.) - Can form a semi-infinite
    interval.     - lower_bound = -infinity: x <= upper_bound.     -
    upper_bound = +infinity: x >= lower_bound. - Can form the infinite
    interval: lower_bound = -infinity and   upper_bound = +infinity, x is free.
    MPVariableProto furthermore stores:  - The coefficient of the variable in
    the objective.  - Whether the variable is integer.
    """

    # lower_bound must be <= upper_bound.
    lower_bound: float = betterproto.double_field(1)
    upper_bound: float = betterproto.double_field(2)
    # The coefficient of the variable in the objective. Must be finite.
    objective_coefficient: float = betterproto.double_field(3)
    # True if the variable is constrained to be integer. Ignored if
    # MPModelProto::solver_type is *LINEAR_PROGRAMMING*.
    is_integer: bool = betterproto.bool_field(4)
    # The name of the variable.
    name: str = betterproto.string_field(5)
    branching_priority: int = betterproto.int32_field(6)


@dataclass
class MPConstraintProto(betterproto.Message):
    """
    A linear constraint is always of the form: lower_bound <= sum of linear
    term elements <= upper_bound, where lower_bound and upper_bound: - Can form
    a singleton: lower_bound == upper_bound. The constraint is an   equation. -
    Can form a finite interval [lower_bound, upper_bound]. The constraint is
    both lower- and upper-bounded, i.e. "boxed". - Can form a semi-infinite
    interval. lower_bound = -infinity: the constraint   is upper-bounded.
    upper_bound = +infinity: the constraint is lower-bounded. - Can form the
    infinite interval: lower_bound = -infinity and   upper_bound = +infinity.
    The constraint is free.
    """

    # var_index[i] is the variable index (w.r.t. to "variable" field of
    # MPModelProto) of the i-th linear term involved in this constraint, and
    # coefficient[i] is its coefficient. Only the terms with non-zero
    # coefficients need to appear. var_index may not contain duplicates.
    var_index: List[int] = betterproto.int32_field(6)
    coefficient: List[float] = betterproto.double_field(7)
    # lower_bound must be <= upper_bound.
    lower_bound: float = betterproto.double_field(2)
    upper_bound: float = betterproto.double_field(3)
    # The name of the constraint.
    name: str = betterproto.string_field(4)
    # [Advanced usage: do not use this if you don't know what you're doing.] A
    # lazy constraint is handled differently by the core solving engine, but it
    # does not change the result. It may or may not impact the performance. For
    # more info see: http://tinyurl.com/lazy-constraints.
    is_lazy: bool = betterproto.bool_field(5)


@dataclass
class MPGeneralConstraintProto(betterproto.Message):
    """
    General constraints. See each individual proto type for more information.
    """

    # The name of the constraint.
    name: str = betterproto.string_field(1)
    indicator_constraint: "MPIndicatorConstraint" = betterproto.message_field(
        2, group="general_constraint"
    )
    sos_constraint: "MPSosConstraint" = betterproto.message_field(
        3, group="general_constraint"
    )
    quadratic_constraint: "MPQuadraticConstraint" = betterproto.message_field(
        4, group="general_constraint"
    )
    abs_constraint: "MPAbsConstraint" = betterproto.message_field(
        5, group="general_constraint"
    )
    # All variables in "and" constraints must be Boolean. resultant_var =
    # and(var_1, var_2... var_n)
    and_constraint: "MPArrayConstraint" = betterproto.message_field(
        6, group="general_constraint"
    )
    # All variables in "or" constraints must be Boolean. resultant_var =
    # or(var_1, var_2... var_n)
    or_constraint: "MPArrayConstraint" = betterproto.message_field(
        7, group="general_constraint"
    )
    # resultant_var = min(var_1, var_2, ..., constant)
    min_constraint: "MPArrayWithConstantConstraint" = betterproto.message_field(
        8, group="general_constraint"
    )
    # resultant_var = max(var_1, var_2, ..., constant)
    max_constraint: "MPArrayWithConstantConstraint" = betterproto.message_field(
        9, group="general_constraint"
    )


@dataclass
class MPIndicatorConstraint(betterproto.Message):
    """
    Indicator constraints encode the activation or deactivation of linear
    constraints given the value of one Boolean variable in the model. For
    example:     y = 0 => 2 * x1 + 3 * x2 >= 42 The 2 * x1 + 3 * x2 >= 42
    constraint is only active if the variable y is equal to 0. As of 2019/04,
    only SCIP, CP-SAT and Gurobi support this constraint type.
    """

    # Variable index (w.r.t. the "variable" field of MPModelProto) of the Boolean
    # variable used as indicator.
    var_index: int = betterproto.int32_field(1)
    # Value the above variable should take. Must be 0 or 1.
    var_value: int = betterproto.int32_field(2)
    # The constraint activated by the indicator variable.
    constraint: "MPConstraintProto" = betterproto.message_field(3)


@dataclass
class MPSosConstraint(betterproto.Message):
    """
    Special Ordered Set (SOS) constraints of type 1 or 2. See
    https://en.wikipedia.org/wiki/Special_ordered_set As of 2019/04, only SCIP
    and Gurobi support this constraint type.
    """

    type: "MPSosConstraintType" = betterproto.enum_field(1)
    # Variable index (w.r.t. the "variable" field of MPModelProto) of the
    # variables in the SOS.
    var_index: List[int] = betterproto.int32_field(2)
    # Optional: SOS weights. If non-empty, must be of the same size as
    # "var_index", and strictly increasing. If empty and required by the
    # underlying solver, the 1..n sequence will be given as weights. SUBTLE: The
    # weights can help the solver make branch-and-bound decisions that fit the
    # underlying optimization model: after each LP relaxation, it will compute
    # the "average weight" of the SOS variables, weighted by value (this is
    # confusing: here we're using the values as weights), and the binary branch
    # decision will be: is the non-zero variable above or below that? (weights
    # are strictly monotonous, so the "cutoff" average weight corresponds to a
    # "cutoff" index in the var_index sequence).
    weight: List[float] = betterproto.double_field(3)


@dataclass
class MPQuadraticConstraint(betterproto.Message):
    """
    Quadratic constraints of the form lb <= sum a_i x_i + sum b_ij x_i x_j <=
    ub, where a, b, lb and ub are constants, and x are the model's variables.
    Quadratic matrices that are Positive Semi-Definite, Second-Order Cones or
    rotated Second-Order Cones are always accepted. Other forms may or may not
    be accepted depending on the underlying solver used. See
    https://scip.zib.de/doc/html/cons__quadratic_8h.php and https://www.gurobi.
    com/documentation/8.1/refman/constraints.html#subsubsection:QuadraticConstr
    aints
    """

    # Sparse representation of linear terms in the quadratic constraint, where
    # term i is var_index[i] * coefficient[i]. `var_index` are variable indices
    # w.r.t the "variable" field in MPModelProto, and should be unique.
    var_index: List[int] = betterproto.int32_field(1)
    coefficient: List[float] = betterproto.double_field(2)
    # Sparse representation of quadratic terms in the quadratic constraint, where
    # term i is qvar1_index[i] * qvar2_index[i] * qcoefficient[i]. `qvar1_index`
    # and `qvar2_index` are variable indices w.r.t the "variable" field in
    # MPModelProto. `qvar1_index`, `qvar2_index` and `coefficients` must have the
    # same size. If the same unordered pair (qvar1_index, qvar2_index) appears
    # several times, the sum of all of the associated coefficients will be
    # applied.
    qvar1_index: List[int] = betterproto.int32_field(3)
    qvar2_index: List[int] = betterproto.int32_field(4)
    qcoefficient: List[float] = betterproto.double_field(5)
    # lower_bound must be <= upper_bound.
    lower_bound: float = betterproto.double_field(6)
    upper_bound: float = betterproto.double_field(7)


@dataclass
class MPAbsConstraint(betterproto.Message):
    """Sets a variable's value to the absolute value of another variable."""

    # Variable indices are relative to the "variable" field in MPModelProto.
    # resultant_var = abs(var)
    var_index: int = betterproto.int32_field(1)
    resultant_var_index: int = betterproto.int32_field(2)


@dataclass
class MPArrayConstraint(betterproto.Message):
    """Sets a variable's value equal to a function on a set of variables."""

    # Variable indices are relative to the "variable" field in MPModelProto.
    var_index: List[int] = betterproto.int32_field(1)
    resultant_var_index: int = betterproto.int32_field(2)


@dataclass
class MPArrayWithConstantConstraint(betterproto.Message):
    """
    Sets a variable's value equal to a function on a set of variables and,
    optionally, a constant.
    """

    # Variable indices are relative to the "variable" field in MPModelProto.
    # resultant_var = f(var_1, var_2, ..., constant)
    var_index: List[int] = betterproto.int32_field(1)
    constant: float = betterproto.double_field(2)
    resultant_var_index: int = betterproto.int32_field(3)


@dataclass
class MPQuadraticObjective(betterproto.Message):
    """
    Quadratic part of a model's objective. Added with other objectives (such as
    linear), this creates the model's objective function to be optimized. Note:
    the linear part of the objective currently needs to be specified in the
    MPVariableProto.objective_coefficient fields. If you'd rather have a
    dedicated linear array here, talk to or-core-team@
    """

    # Sparse representation of quadratic terms in the objective function, where
    # term i is qvar1_index[i] * qvar2_index[i] * coefficient[i]. `qvar1_index`
    # and `qvar2_index` are variable indices w.r.t the "variable" field in
    # MPModelProto. `qvar1_index`, `qvar2_index` and `coefficients` must have the
    # same size. If the same unordered pair (qvar1_index, qvar2_index) appears
    # several times, the sum of all of the associated coefficients will be
    # applied.
    qvar1_index: List[int] = betterproto.int32_field(1)
    qvar2_index: List[int] = betterproto.int32_field(2)
    coefficient: List[float] = betterproto.double_field(3)


@dataclass
class PartialVariableAssignment(betterproto.Message):
    """
    This message encodes a partial (or full) assignment of the variables of a
    MPModelProto problem. The indices in var_index should be unique and valid
    variable indices of the associated problem.
    """

    var_index: List[int] = betterproto.int32_field(1)
    var_value: List[float] = betterproto.double_field(2)


@dataclass
class MPModelProto(betterproto.Message):
    """
    MPModelProto contains all the information for a Linear Programming model.
    """

    # All the variables appearing in the model.
    variable: List["MPVariableProto"] = betterproto.message_field(3)
    # All the constraints appearing in the model.
    constraint: List["MPConstraintProto"] = betterproto.message_field(4)
    # All the general constraints appearing in the model. Note that not all
    # solvers support all types of general constraints.
    general_constraint: List["MPGeneralConstraintProto"] = betterproto.message_field(7)
    # True if the problem is a maximization problem. Minimize by default.
    maximize: bool = betterproto.bool_field(1)
    # Offset for the objective function. Must be finite.
    objective_offset: float = betterproto.double_field(2)
    # Optionally, a quadratic objective. As of 2019/06, only SCIP and Gurobi
    # support quadratic objectives.
    quadratic_objective: "MPQuadraticObjective" = betterproto.message_field(8)
    # Name of the model.
    name: str = betterproto.string_field(5)
    # Solution hint. If a feasible or almost-feasible solution to the problem is
    # already known, it may be helpful to pass it to the solver so that it can be
    # used. A solver that supports this feature will try to use this information
    # to create its initial feasible solution. Note that it may not always be
    # faster to give a hint like this to the solver. There is also no guarantee
    # that the solver will use this hint or try to return a solution "close" to
    # this assignment in case of multiple optimal solutions.
    solution_hint: "PartialVariableAssignment" = betterproto.message_field(6)


@dataclass
class OptionalDouble(betterproto.Message):
    """
    To support 'unspecified' double value in proto3, the simplest is to wrap
    any double value in a nested message (has_XXX works for message fields). We
    don't use google/protobuf/wrappers.proto because depending on it makes the
    following android integration test fail:
    http://sponge/c4bce1fd-41bd-4d0b-b4ca-fc04d4d64621
    """

    value: float = betterproto.double_field(1)


@dataclass
class MPSolverCommonParameters(betterproto.Message):
    """
    MPSolverCommonParameters holds advanced usage parameters that apply to any
    of the solvers we support. All of the fields in this proto can have a value
    of unspecified. In this case each inner solver will use their own safe
    defaults. Some values won't be supported by some solvers. The behavior in
    that case is not defined yet.
    """

    # The solver stops if the relative MIP gap reaches this value or below. The
    # relative MIP gap is an upper bound of the relative distance to the optimum,
    # and it is defined as:   abs(best_bound - incumbent) / abs(incumbent)
    # [Gurobi]   abs(best_bound - incumbent) / min(abs(best_bound),
    # abs(incumbent)) [SCIP] where "incumbent" is the objective value of the best
    # solution found so far (i.e., lowest when minimizing, highest when
    # maximizing), and "best_bound" is the tightest bound of the objective
    # determined so far (i.e., highest when minimizing, and lowest when
    # maximizing). The MIP Gap is sensitive to objective offset. If the
    # denominator is 0 the MIP Gap is INFINITY for SCIP and Gurobi. Of note,
    # "incumbent" and "best bound" are called "primal bound" and "dual bound" in
    # SCIP, respectively. Ask or-core-team@ for other solvers.
    relative_mip_gap: "OptionalDouble" = betterproto.message_field(1)
    # Tolerance for primal feasibility of basic solutions: this is the maximum
    # allowed error in constraint satisfiability. For SCIP this includes
    # integrality constraints. For Gurobi it does not, you need to set the custom
    # parameter IntFeasTol.
    primal_tolerance: "OptionalDouble" = betterproto.message_field(2)
    # Tolerance for dual feasibility. For SCIP and Gurobi this is the feasibility
    # tolerance for reduced costs in LP solution: reduced costs must all be
    # smaller than this value in the improving direction in order for a model to
    # be declared optimal. Not supported for other solvers.
    dual_tolerance: "OptionalDouble" = betterproto.message_field(3)
    # Algorithm to solve linear programs. Ask or-core-team@ if you want to know
    # what this does exactly.
    lp_algorithm: "MPSolverCommonParametersLPAlgorithmValues" = betterproto.enum_field(
        4
    )
    # Gurobi and SCIP enable presolve by default. Ask or-core-team@ for other
    # solvers.
    presolve: "OptionalBoolean" = betterproto.enum_field(5)
    # Enable automatic scaling of matrix coefficients and objective. Available
    # for Gurobi and GLOP. Ask or-core-team@ if you want more details.
    scaling: "OptionalBoolean" = betterproto.enum_field(7)


@dataclass
class MPModelDeltaProto(betterproto.Message):
    """
    Encodes a full MPModelProto by way of referencing to a "baseline"
    MPModelProto stored in a file, and a "delta" to apply to this model.
    """

    baseline_model_file_path: str = betterproto.string_field(1)
    # The variable protos listed here will override (via MergeFrom()) the ones in
    # the baseline model: you only need to specify the fields that change. To add
    # a new variable, add it with a new variable index (variable indices still
    # need to span a dense integer interval). You can't "delete" a variable but
    # you can "neutralize" it by fixing its value, setting its objective
    # coefficient to zero, and by nullifying all the terms involving it in the
    # constraints.
    variable_overrides: Dict[int, "MPVariableProto"] = betterproto.map_field(
        2, betterproto.TYPE_INT32, betterproto.TYPE_MESSAGE
    )
    # Constraints can be changed (or added) in the same way as variables, see
    # above. It's mostly like applying MergeFrom(), except that: - the
    # "var_index" and "coefficient" fields will be overridden like a map:   if a
    # key pre-exists, we overwrite its value, otherwise we add it. - if you set
    # the lower bound to -inf and the upper bound to +inf, thus   effectively
    # neutralizing the constraint, the solver will implicitly   remove all of the
    # constraint's terms.
    constraint_overrides: Dict[int, "MPConstraintProto"] = betterproto.map_field(
        3, betterproto.TYPE_INT32, betterproto.TYPE_MESSAGE
    )


@dataclass
class MPModelRequest(betterproto.Message):
    """Next id: 9."""

    # The model to be optimized by the server.
    model: "MPModelProto" = betterproto.message_field(1)
    solver_type: "MPModelRequestSolverType" = betterproto.enum_field(2)
    # Maximum time to be spent by the solver to solve 'model'. If the server is
    # busy and the RPC's deadline_left is less than this, it will immediately
    # give up and return an error, without even trying to solve. The client can
    # use this to have a guarantee on how much time the solver will spend on the
    # problem (unless it finds and proves an optimal solution more quickly). If
    # not specified, the time limit on the solver is the RPC's deadline_left.
    solver_time_limit_seconds: float = betterproto.double_field(3)
    # If this is set, then EnableOutput() will be set on the internal MPSolver
    # that solves the model. WARNING: if you set this on a request to prod
    # servers, it will be rejected and yield the RPC Application Error code
    # MPSOLVER_SOLVER_TYPE_UNAVAILABLE.
    enable_internal_solver_output: bool = betterproto.bool_field(4)
    # Advanced usage. Solver-specific parameters in the solver's own format,
    # different for each solver. For example, if you use SCIP and you want to
    # stop the solve earlier than the time limit if it reached a solution that is
    # at most 1% away from the optimal, you can set this to "limits/gap=0.01".
    # Note however that there is no "security" mechanism in place so it is up to
    # the client to make sure that the given options don't make the solve non
    # thread safe or use up too much memory for instance. If the option format is
    # not understood by the solver, the request will be rejected and yield an RPC
    # Application error with code MPSOLVER_MODEL_INVALID_SOLVER_PARAMETERS.
    solver_specific_parameters: str = betterproto.string_field(5)
    # Advanced usage: model "delta". If used, "model" must be unset. See the
    # definition of MPModelDeltaProto.
    model_delta: "MPModelDeltaProto" = betterproto.message_field(8)


@dataclass
class MPSolutionResponse(betterproto.Message):
    # Result of the optimization.
    status: "MPSolverResponseStatus" = betterproto.enum_field(1)
    # Human-readable string giving more details about the status. For example,
    # when the status is MPSOLVER_INVALID_MODE, this can hold a description of
    # why the model is invalid. This isn't always filled: don't depend on its
    # value or even its presence.
    status_str: str = betterproto.string_field(7)
    # Objective value corresponding to the "variable_value" below, taking into
    # account the source "objective_offset" and "objective_coefficient". This is
    # set iff 'status' is OPTIMAL or FEASIBLE.
    objective_value: float = betterproto.double_field(2)
    # This field is only filled for MIP problems. For a minimization problem,
    # this is a lower bound on the optimal objective value. For a maximization
    # problem, it is an upper bound. It is only filled if the status is OPTIMAL
    # or FEASIBLE. In the former case, best_objective_bound should be equal to
    # objective_value (modulo numerical errors).
    best_objective_bound: float = betterproto.double_field(5)
    # Variable values in the same order as the MPModelProto::variable field. This
    # is a dense representation. These are set iff 'status' is OPTIMAL or
    # FEASIBLE.
    variable_value: List[float] = betterproto.double_field(3)
    # [Advanced usage.] Values of the dual variables values in the same order as
    # the MPModelProto::constraint field. This is a dense representation. These
    # are not set if the problem was solved with a MIP solver (even if it is
    # actually a linear program). These are set iff 'status' is OPTIMAL or
    # FEASIBLE.
    dual_value: List[float] = betterproto.double_field(4)
    # [Advanced usage.] Values of the reduced cost of the variables in the same
    # order as the MPModelProto::variable. This is a dense representation. These
    # are not set if the problem was solved with a MIP solver (even if it is
    # actually a linear program). These are set iff 'status' is OPTIMAL or
    # FEASIBLE.
    reduced_cost: List[float] = betterproto.double_field(6)


@dataclass
class ReferenceMPVariable(betterproto.Message):
    var_name: str = betterproto.string_field(5)
    model_name: str = betterproto.string_field(6)
    var_index: int = betterproto.int32_field(7)
    reference_name: str = betterproto.string_field(8)
    tags: List[str] = betterproto.string_field(11)


@dataclass
class MPExpression(betterproto.Message):
    name: str = betterproto.string_field(5)
    lower_bound: float = betterproto.double_field(6)
    upper_bound: float = betterproto.double_field(7)
    objective_coefficient: float = betterproto.double_field(8)
    variables: List["ReferenceMPVariable"] = betterproto.message_field(11)
    variables_names: List[str] = betterproto.string_field(10)
    # do we really need this vairables_names field? they do exist inside the
    # variables already,no?
    variable_coefficients: List[float] = betterproto.double_field(12)
    tags: List[str] = betterproto.string_field(15)


@dataclass
class ExpressionMPModel(betterproto.Message):
    variable: List["MPVariableProto"] = betterproto.message_field(3)
    constraint: List["MPConstraintProto"] = betterproto.message_field(4)
    general_constraint: List["MPGeneralConstraintProto"] = betterproto.message_field(7)
    maximize: bool = betterproto.bool_field(1)
    objective_offset: float = betterproto.double_field(2)
    quadratic_objective: "MPQuadraticObjective" = betterproto.message_field(8)
    name: str = betterproto.string_field(5)
    solution_hint: "PartialVariableAssignment" = betterproto.message_field(6)
    expressions: List["MPExpression"] = betterproto.message_field(11)
    reference_constraints: List["ReferenceMPConstraint"] = betterproto.message_field(12)


@dataclass
class ReferenceMPConstraint(betterproto.Message):
    lower_bound: float = betterproto.double_field(2)
    upper_bound: float = betterproto.double_field(3)
    name: str = betterproto.string_field(4)
    variable_coefficients: List[float] = betterproto.double_field(7)
    variable_references: List["ReferenceMPVariable"] = betterproto.message_field(8)


@dataclass
class ReferenceMPModel(betterproto.Message):
    name: str = betterproto.string_field(5)
    variables: List["MPVariableProto"] = betterproto.message_field(3)
    constraints: List["MPConstraintProto"] = betterproto.message_field(4)
    maximize: bool = betterproto.bool_field(1)
    reference_variables: List["ReferenceMPVariable"] = betterproto.message_field(10)
    reference_constraints: List["ReferenceMPConstraint"] = betterproto.message_field(11)
    # double objective_offset = 2 [default = 0.0]; having the var references,
    # does expressions help here? I
    expressions: List["MPExpression"] = betterproto.message_field(15)
    tags: List[str] = betterproto.string_field(16)
    model_dependencies: List[str] = betterproto.string_field(17)
    build_final: bool = betterproto.bool_field(20)


@dataclass
class ExtendedMPModel(betterproto.Message):
    concrete_model: "MPModelProto" = betterproto.message_field(1)
    reference_model: "ReferenceMPModel" = betterproto.message_field(2)
    expression_model: "ExpressionMPModel" = betterproto.message_field(3)


@dataclass
class ReferenceMPModelRequest(betterproto.Message):
    # The model to be optimized by the server.
    model: "ExtendedMPModel" = betterproto.message_field(1)


@dataclass
class ReferenceMPModelResponse(betterproto.Message):
    response: "ExtendedMPModelResponse" = betterproto.message_field(1)


@dataclass
class ExtendedMPModelResponse(betterproto.Message):
    name: str = betterproto.string_field(1)
    concrete_response: "MPSolutionResponse" = betterproto.message_field(2)
    reference_response: "ReferenceSolutionResponse" = betterproto.message_field(3)


@dataclass
class ReferenceSolutionResponse(betterproto.Message):
    solver_model_solution: "MPSolutionResponse" = betterproto.message_field(1)
    solver_model_request: "MPModelProto" = betterproto.message_field(2)
    variable_value: List["NamedValue"] = betterproto.message_field(3)
    expression_value: List["NamedValue"] = betterproto.message_field(4)


@dataclass
class NamedValue(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: float = betterproto.double_field(2)
