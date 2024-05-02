import { ParserDatabase } from '@baml/common'
import { BamlWasm } from '.'
import { handleFormatPanic, handleWasmError } from './internals'

type LintResponse = {
  diagnostics: LinterError[]
} & (
    | { ok: false }
    | {
      ok: true
      response: ParserDatabase
    }
  )

export interface LinterError {
  start: number
  end: number
  text: string
  is_warning: boolean
  source_file: string
}

export interface LinterSourceFile {
  path: string
  content: string
}

export interface LinterInput {
  root_path: string
  files: LinterSourceFile[]
  // Function Name -> Test Name
  selected_tests: Record<string, string>
}

export default function lint(input: LinterInput, onError?: (errorMessage: string) => void): LintResponse {
  try {
    if (process.env.FORCE_PANIC_baml_SCHEMA) {
      handleFormatPanic(() => {
        console.debug('Triggering a Rust panic...')
        BamlWasm.debug_panic()
      })
    }


    const result = BamlWasm.lint(JSON.stringify(input))
    const parsed = JSON.parse(result) as LintResponse
    // console.log(`lint result ${JSON.stringify(JSON.parse(result), null, 2)}`)
    return parsed
  } catch (e) {
    const err = e as Error

    handleWasmError(err, 'lint', onError)

    return {
      ok: false,
      diagnostics: [],
    }
  }
}
