export type str = string
export type int = number
export type float = number
export type bool = boolean
export type List<T> = Array<T>
export type Dict<K extends keyof any = string, V = any> = {
    [key in K extends string | number ? K : string]: V;
}
export type None = null | undefined
export type Tuple<T extends any[]> = T
export type Union<T> = T
export type Literal<T extends string | number | boolean> = T
export type Optional<T> = T | undefined
export type Any = any
export type Callable<T extends any[], R> = (...args: T) => R
