# ROADMAP.md

## Overview
`code-verifier` is an Axentx product designed to deliver high-accuracy AI code generation, prioritizing correctness over speed. The tool integrates automated testing and verification pipelines to ensure generated code meets required standards, enabling developers to produce reliable software with minimal manual validation effort.

## MVP Milestone (Launch Ready)
The Minimum Viable Product will focus on core verification capabilities to validate the product's value proposition. All MVP-critical features must be fully functional and tested.

### MVP Features
1. **Core Model Integration**  
   - Deploy a production-ready inference engine using `vLLM` (verified via `vllm-project/vllm`) to run the code verification model.  
   - MVP-critical: Ensures reliable execution of verification logic.  
2. **Basic Test Generation**  
   - Generate unit tests for provided code snippets using structured generation (e.g., `sglang` from `sgl-project/sglang`).  
   - MVP-critical: Enables automated testing of code correctness.  
3. **Verification Pipeline**  
   - Execute generated tests and validate code against expected outcomes.  
   - MVP-critical: Core functionality to confirm code meets requirements.  
4. **User Interface**  
   - Simple web UI (or CLI) to upload code, run verification, and view results.  
   - MVP-critical: Provides an accessible entry point for users.  

## Phase 1: Version 1 (Expansion of Core Capabilities)
Focus on broadening test coverage and improving user experience.

### Phase 1 Themes
- **Enhanced Test Coverage**  
  - Add support for integration tests and edge-case scenarios.  
  - Integrate with popular testing frameworks (e.g., Jest, pytest).  
- **Multi-Language Support**  
  - Extend model training to include additional languages (e.g., Python, JavaScript, Go).  
  - MVP-critical: Aligns with existing portfolio (e.g., iceoryx2 supports C++).  
- **IDE Integration**  
  - Develop plugins for major IDEs (VS Code, IntelliJ) to enable inline verification.  

## Phase 2: Version 2 (Advanced Features & Enterprise Readiness)
Introduce enterprise-grade capabilities and performance optimizations.

### Phase 2 Themes
- **Static Analysis Integration**  
  - Integrate with static analysis tools (e.g., SonarQube, ESLint) to flag code vulnerabilities.  
- **Performance Optimization**  
  - Optimize inference speed while maintaining accuracy (leveraging `vLLM` batching and model quantization).  
- **Enterprise Features**  
  - Add team collaboration, audit logs, and role-based access control.  

## Future Phases
- **Code Refactoring Suggestions**  
  - Provide recommendations to improve code quality and maintainability.  
- **Continuous Integration Deep Integration**  
  - Seamlessly integrate with CI/CD pipelines (e.g., GitHub Actions, Jenkins).  

## Dependencies & Frameworks
- **Inference Engine**: `vLLM` (github.com/vllm-project/vllm)  
- **Structured Generation**: `sglang` (github.com/sgl-project/sglang)  
- **Data**: Utilize existing datasets (e.g., `auto`, `messages`, `instr-resp`) for model training and validation.  

## Metrics for Success
- **MVP**: >80%
