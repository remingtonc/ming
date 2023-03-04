import replace from "@rollup/plugin-replace";
import terser from "@rollup/plugin-terser";
import { nodeResolve } from "@rollup/plugin-node-resolve"

export default {
    input: "index.js",
    output: [
        {
            file: "../ming/routes/static/js/tiptap-rollup.js",
            format: "iife",
            name: "window",
            extend: true
        },
        {
            file: "../ming/routes/static/js/tiptap-rollup.min.js",
            format: "iife",
            name: "window",
            extend: true,
            plugins: [ terser() ]
        }
    ],
    plugins: [
        replace({
            "process.env.NODE_ENV": "'production'",
            "preventAssignment": true
        }),
        nodeResolve()
    ]
};
