import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Configuration (Website Layout)
st.set_page_config(page_title="Study of Machine Learning", layout="wide")

# 2. Initialize Navigation State (Computer ko page yaad rakhne ke liye)
if "page" not in st.session_state:
    st.session_state.page = "home"
if "ml_type" not in st.session_state:
    st.session_state.ml_type = None
if "selected_algo" not in st.session_state:
    st.session_state.selected_algo = None

# ==========================================
# LEVEL 1: HOME PAGE
# ==========================================
if st.session_state.page == "home":
    st.markdown(
        "<h1 style='text-align: center; color: #1E3A8A; font-family: sans-serif;'>🎓 Study of Machine Learning</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 20px; color: #555;'>An Interactive Roadmap to Master ML Algorithms</p>",
        unsafe_allow_html=True)
    st.write("---")

    # Developer Profile
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("### 🧑‍💻 Developer Profile")
        st.markdown("🚀 **Created By:** **Sujit Kumar**")
        st.markdown("🎯 **Role:** Aspiring Data Scientist")
        st.write(
            "Welcome to my personal Machine Learning repository. I am building this platform to break down complex concepts into simple English.")

    with col_right:
        st.info(
            "🧠 **My Vision:** Simple English logic, clear mathematical visualization, and clean production-ready code.")

    st.write("---")

    # Next Page Button
    if st.button("Explore Machine Learning Types ➡️", use_container_width=True):
        st.session_state.page = "ml_types"
        st.rerun()
# ==========================================
# LEVEL 2: ML TYPES SECTION
# ==========================================
elif st.session_state.page == "ml_types":
    st.title("🤖 Select Machine Learning Type")
    st.write("Choose a category to explore its core algorithms:")
    st.write("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🟩 Supervised Learning")
        st.write("The model learns from labeled data (Input + Correct Output). Used for Regression & Classification.")
        if st.button("Open Supervised Algorithms", use_container_width=True):
            st.session_state.page = "algo_menu"
            st.session_state.ml_type = "supervised"
            st.rerun()

    with col2:
        st.markdown("### 🟦 Unsupervised Learning")
        st.write(
            "The model learns from unlabeled data to find hidden patterns. Used for Clustering & Dimension Reduction.")
        if st.button("Open Unsupervised Algorithms", use_container_width=True):
            st.session_state.page = "algo_menu"
            st.session_state.ml_type = "unsupervised"
            st.rerun()

    with col3:
        st.markdown("### 🟨 Reinforcement Learning")
        st.write(
            "The model learns by interacting with an environment through trial-and-error using rewards & penalties.")
        if st.button("Open Reinforcement Section", use_container_width=True):
            st.session_state.page = "algo_menu"
            st.session_state.ml_type = "reinforcement"
            st.rerun()

    st.write("\n")
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
# ==========================================
# LEVEL 3: ALGORITHM MENU
# ==========================================
elif st.session_state.page == "algo_menu":
    if st.session_state.ml_type == "supervised":
        st.title("🟩 Supervised Learning Algorithms")
        st.write("Select an international standard algorithm to study:")
        st.write("---")

        selected = st.selectbox("Choose Algorithm:", [
            "-- Select --",
            "Linear Regression",
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Support Vector Machines (SVM)",
            "K-Nearest Neighbors (KNN)"
        ])

        if selected != "-- Select --":
            st.session_state.page = "deep_dive"
            st.session_state.selected_algo = selected
            st.rerun()

    elif st.session_state.ml_type == "unsupervised":
        st.title("🟦 Unsupervised Learning Algorithms")
        st.write("Select an algorithm to deep dive into pattern discovery:")
        st.write("---")

        selected = st.selectbox("Choose Algorithm:", [
            "-- Select --",
            "K-Means Clustering",
            "Hierarchical Clustering",
            "Principal Component Analysis (PCA)",
            "Isolation Forest"
        ])

        if selected != "-- Select --":
            st.session_state.page = "deep_dive"
            st.session_state.selected_algo = selected
            st.rerun()

    elif st.session_state.ml_type == "reinforcement":
        st.title("🟨 Reinforcement Learning")
        st.write("Explore autonomous learning systems:")
        st.write("---")

        selected = st.selectbox("Choose Concept/Algorithm:", [
            "-- Select --",
            "Q-Learning (Core Concept)"
        ])

        if selected != "-- Select --":
            st.session_state.page = "deep_dive"
            st.session_state.selected_algo = selected
            st.rerun()

    st.write("\n")
    if st.button("⬅️ Back to ML Types"):
        st.session_state.page = "ml_types"
        st.rerun()
# ==========================================
# LEVEL 4: FINAL DEEP DIVE (CONCEPTS & CODE)
# ==========================================
elif st.session_state.page == "deep_dive":
    st.title(f"🚀 Algorithm Deep Dive: {st.session_state.selected_algo}")
    st.write("---")

    # ----------------------------------------------------
    # BLOCK A: LINEAR REGRESSION COMPLETE DATA
    # ----------------------------------------------------
    if st.session_state.selected_algo == "Linear Regression":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Linear Regression?")
            st.write("""
            Linear Regression is a fundamental Supervised Learning algorithm used to predict a **Continuous Numerical Value** 
            based on one or more input features. It assumes a straight-line relationship between inputs and outputs.
            """)

            st.markdown("#### 🧮 The Core Mathematical Formula:")
            st.latex(r"y = mx + c")

            st.markdown("""
            * **$y$ (Dependent Variable):** The target variable you want to predict (e.g., House Price).
            * **$x$ (Independent Variable):** The input feature you provide to the model (e.g., House Size in SqFt).
            * **$m$ (Slope / Weight):** Represents the relationship strength; tells how much $y$ changes when $x$ changes by 1 unit.
            * **$c$ (Intercept / Bias):** The starting point; the expected value of $y$ when $x$ is equal to 0.
            """)

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Real Estate:** Predicting apartment prices based on square footage and location.")
            st.write("- **Business:** Forecasting future sales revenue based on monthly marketing expenses.")
            st.write("- **HR Metrics:** Estimating an employee's salary based on years of experience.")

            st.info(
                "💡 **Interview Alert:** The main objective of Linear Regression is to find the **Line of Best Fit** by minimizing the distance between actual data points and the predicted line using a cost function called **Mean Squared Error (MSE)**.")

        with tab2:
            st.markdown("### 📈 Interactive Training Simulation")
            st.write(
                "Adjust the Sliders below to manually fit the red regression line onto the actual blue data points. See how the Error (MSE) changes live!")

            m_slider = st.slider("Adjust Slope (m)", min_value=-5.0, max_value=5.0, value=1.0, step=0.2)
            c_slider = st.slider("Adjust Intercept (c)", min_value=-10, max_value=10, value=2, step=1)

            np.random.seed(42)
            x_data = np.linspace(-5, 5, 40)
            y_noise = np.random.normal(0, 3, 40)
            y_actual = 2.5 * x_data + 3 + y_noise

            y_predicted = m_slider * x_data + c_slider
            mse_score = np.mean((y_actual - y_predicted) ** 2)

            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(x_data, y_actual, color="#1E3A8A", label="Actual Data Points", alpha=0.7)
            ax.plot(x_data, y_predicted, color="#FF4B4B", linewidth=2.5,
                    label=f"Your Line: y = {m_slider}x + {c_slider}")
            ax.set_xlabel("Input Feature (x)")
            ax.set_ylabel("Target Output (y)")
            ax.legend(loc="upper left")
            ax.grid(True, linestyle="--", alpha=0.6)
            st.pyplot(fig)

            if mse_score < 12.0:
                st.success(
                    f"🏆 Fantastic Fit! Current Mean Squared Error (MSE): **{mse_score:.2f}** (Very close to optimal!)")
            else:
                st.error(
                    f"❌ High Error! Current Mean Squared Error (MSE): **{mse_score:.2f}**. Try adjusting the sliders to bring the line closer to points (Hint: m around 2.4, c around 3).")

        with tab3:
            st.markdown("### 💻 Clean Production-Ready Code Template")
            st.write(
                "This is the standard code structure used in international industries to build and train a Linear Regression model using **Scikit-Learn**:")

            lr_code = """
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Preparing the Data (Features must be 2D array, Targets must be 1D)
X_train = np.array([[1], [2], [3], [4], [5]])  # Features (e.g., Experience)
y_train = np.array([5, 7, 9, 11, 13])          # Target (e.g., Salary)

# 2. Initializing the Model
model = LinearRegression()

# 3. Training the Model (Fitting the line to the data)
model.fit(X_train, y_train)

# 4. Checking Learned Parameters (Weights and Bias)
print(f"Learned Slope (m): {model.coef_[0]:.2f}")
print(f"Learned Intercept (c): {model.intercept_:.2f}")

# 5. Making Predictions on New Unseen Data
new_input = np.array([[6]])  # Predicting for 6 years of experience
prediction = model.predict(new_input)
print(f"Prediction for input 6: ${prediction[0]:.2f}")
            """
            st.code(lr_code, language="python")
            st.caption("💡 Tip: You can directly copy this block and use it in your data science pipelines.")
    elif st.session_state.selected_algo == "Logistic Regression":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Logistic Regression?")
            st.write("""
                  Logistic Regression is a core Supervised Learning algorithm used for **Classification tasks** (predicting categorical classes like Yes/No, Spam/Not Spam, Fraud/Safe). 
                  Unlike Linear Regression which predicts numbers, Logistic Regression predicts the **probability** of an event occurring between 0 and 1.
                  """)

            st.markdown("#### 🧮 The Sigmoid Function Formula:")
            st.latex(r"P = \frac{1}{1 + e^{-y}} \quad \text{where } y = mx + c")
            st.write(
                "The **Sigmoid Function** takes any real-valued number and squashes it into a probability value between **0 and 1**.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Healthcare:** Predicting whether a patient has a specific disease (Positive/Negative).")
            st.write("- **Cybersecurity:** Detecting if an email is Spam or Ham.")
            st.write(
                "- **Banking:** Assessing credit risk to decide if a loan application should be Approved or Rejected.")

            st.info(
                "💡 **Interview Alert:** Logistic Regression uses a threshold (usually 0.5). If the probability is greater than 0.5, it classifies it as Class 1 (Yes); otherwise, Class 0 (No). It optimizes parameters using a cost function called **Log Loss** or **Binary Cross-Entropy**.")

        with tab2:
            st.markdown("### 📈 Interactive Sigmoid S-Curve")
            st.write(
                "Adjust the slider to see how changing the intercept impacts the Sigmoid activation function. Notice how it always stays bounded between 0 and 1.")

            shift_slider = st.slider("Shift Sigmoid Horizontal Axis", min_value=-5.0, max_value=5.0, value=0.0,
                                     step=0.5)

            x_sig = np.linspace(-10, 10, 100)
            y_sig = 1 / (1 + np.exp(-(x_sig - shift_slider)))

            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.plot(x_sig, y_sig, color="#FF4B4B", linewidth=2.5, label="Sigmoid Curve")
            ax.axhline(0.5, color="gray", linestyle="--", alpha=0.5, label="0.5 Threshold")
            ax.axvline(shift_slider, color="blue", linestyle=":", alpha=0.5)
            ax.set_xlabel("Input Value (z)")
            ax.set_ylabel("Calculated Probability (P)")
            ax.legend(loc="upper left")
            ax.grid(True, linestyle="--", alpha=0.6)
            st.pyplot(fig)

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write("Standard implementation for training a binary classifier using **Scikit-Learn**:")

            log_code = """
      import numpy as np
      from sklearn.linear_model import LogisticRegression

      # 1. Training Data (Features and Categories: 0 or 1)
      X_train = np.array([[1], [2], [3], [4], [5]]) # Inputs
      y_train = np.array([0, 0, 0, 1, 1])       # Target Labels (0=No, 1=Yes)

      # 2. Initializing & Training Classifier
      classifier = LogisticRegression()
      classifier.fit(X_train, y_train)

      # 3. Predict Exact Probabilities
      new_sample = np.array([[3.5]])
      prob = classifier.predict_proba(new_sample)
      print(f"Probabilities [Class 0, Class 1]: {prob}")

      # 4. Predict Final Category Class (0 or 1)
      prediction = classifier.predict(new_sample)
      print(f"Final Class Prediction: {prediction}")
                  """
            st.code(log_code, language="python")


    elif st.session_state.selected_algo == "Decision Tree":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is a Decision Tree?")
            st.write("""
                A Decision Tree is a non-parametric Supervised Learning algorithm used for both **Classification and Regression** tasks. 
                It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. 
                The final result is a tree with **decision nodes** (e.g., Is Income > $50k?) and **leaf nodes** (e.g., Approve Loan).
                """)

            st.markdown("#### 🧮 The Mathematics Behind Splits:")
            st.write("Decision Trees choose the best feature to split data based on metrics that measure impurity:")

            st.markdown("**1. Entropy (Measure of Randomness/Chaos):**")
            st.latex(r"Entropy(S) = - \sum_{i=1}^{c} p_i \log_2 p_i")

            st.markdown("**2. Gini Impurity (Probability of misclassification - Default in Scikit-Learn):**")
            st.latex(r"Gini = 1 - \sum_{i=1}^{c} (p_i)^2")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Banking:** Customer churn prediction (Will the customer leave the bank or stay?).")
            st.write("- **E-commerce:** Recommendation systems based on user demographic features.")
            st.write("- **Medical:** Diagnosis systems predicting a disease based on a chain of symptoms.")

            st.info(
                "💡 **Interview Alert:** Decision Trees are prone to **Overfitting** (learning the training data too perfectly, causing poor test accuracy). To prevent this, we use techniques like **Pruning** or restrict parameters like `max_depth` or `min_samples_split`.")

        with tab2:
            st.markdown("### 📈 Interactive Node Splitting (Tree Depth)")
            st.write(
                "Adjust the maximum depth slider to see how a Decision Tree boundary splits data. Higher depth means complex, tightly bounded rules (High risk of Overfitting).")

            depth_slider = st.slider("Max Tree Depth (max_depth)", min_value=1, max_value=5, value=2, step=1)

            # Generating Dummy Data for Classification
            np.random.seed(10)
            X_tree = np.random.randn(100, 2)
            # Create a simple non-linear boundary
            y_tree = (X_tree[:, 0] * X_tree[:, 1] > 0.1).astype(int)

            # Fitting a live dummy model to plot boundaries
            from sklearn.tree import DecisionTreeClassifier

            clf = DecisionTreeClassifier(max_depth=depth_slider, random_state=42)
            clf.fit(X_tree, y_tree)

            # Plotting the data points
            fig, ax = plt.subplots(figsize=(6, 3.2))
            scatter = ax.scatter(X_tree[:, 0], X_tree[:, 1], c=y_tree, cmap="coolwarm", edgecolors='k', alpha=0.8)
            ax.set_xlabel("Feature 1 (X1)")
            ax.set_ylabel("Feature 2 (X2)")
            ax.set_title(f"Data Splits at Depth = {depth_slider}")
            ax.grid(True, linestyle="--", alpha=0.5)

            st.pyplot(fig)
            st.caption(
                "💡 Notice how changing the depth creates horizontal or vertical division rules to separate red and blue dots.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write(
                "Standard code structure to train a Decision Tree Classifier with regularization parameter (`max_depth`) using **Scikit-Learn**:")

            tree_code = """
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import make_classification

    # 1. Generate Synthetic Classification Data
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)

    # 2. Initializing the Model (Setting max_depth prevents Overfitting)
    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

    # 3. Training the Model
    model.fit(X, y)

    # 4. Checking Feature Importances (Which column was most useful?)
    for col, importance in zip(['Feat1', 'Feat2', 'Feat3', 'Feat4'], model.feature_importances_):
        print(f"{col}: {importance:.2f}")

    # 5. Predict Class for a New Record
    new_data = [[0.5, -1.2, 2.1, 0.3]]
    prediction = model.predict(new_data)
    print(f"Predicted Class Label: {prediction}")
                """
            st.code(tree_code, language="python")


    elif st.session_state.selected_algo == "Random Forest":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Random Forest?")
            st.write("""
                Random Forest is an **Ensemble Learning** algorithm that combines multiple Decision Trees to make a more accurate and stable prediction. 
                Instead of relying on just one tree, it trains a collection (a 'forest') of independent trees and aggregates their outputs.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood:")
            st.write("Random Forest relies on two key concepts to reduce overfitting:")
            st.markdown(
                "1. **Bagging (Bootstrap Aggregating):** It creates multiple subsets of data by selecting random rows with replacement. Each tree gets a different subset.")
            st.markdown(
                "2. **Feature Randomization:** When splitting nodes, it only considers a random subset of columns/features. This ensures the trees are very diverse.")
            st.markdown(
                "3. **Voting/Averaging:** For Classification, it takes the **Majority Vote** of all trees. For Regression, it takes the **Average**.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Finance:** Fraud detection in credit card transactions (Highly robust to outliers).")
            st.write("- **Healthcare:** Predicting patient readmission risk using high-dimensional medical records.")
            st.write("- **E-commerce:** Predicting whether a user will buy a product based on their search history.")

            st.info(
                "💡 **Interview Alert:** Random Forest natively solves the major drawback of individual Decision Trees: **Overfitting**. By averaging results from hundreds of diverse trees, it reduces the overall *Variance* without increasing the *Bias*.")

        with tab2:
            st.markdown("### 📈 Interactive Forest Simulation (Number of Trees)")
            st.write(
                "Adjust the number of estimators (trees) to see how combining more trees creates a smoother, more reliable decision boundary.")

            n_trees_slider = st.slider("Number of Trees (n_estimators)", min_value=1, max_value=50, value=5, step=5)

            # Generating Dummy Complex Data
            np.random.seed(42)
            X_rf = np.random.randn(120, 2)
            y_rf = (X_rf[:, 0] ** 2 + X_rf[:, 1] ** 2 > 0.6).astype(int)

            # Fitting Random Forest Classifier
            from sklearn.ensemble import RandomForestClassifier

            rf_clf = RandomForestClassifier(n_estimators=n_trees_slider, max_depth=3, random_state=42)
            rf_clf.fit(X_rf, y_rf)

            # Plotting the data boundaries
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(X_rf[:, 0], X_rf[:, 1], c=y_rf, cmap="coolwarm", edgecolors='k', alpha=0.8)
            ax.set_xlabel("Feature 1")
            ax.set_ylabel("Feature 2")
            ax.set_title(f"Random Forest Boundary with {n_trees_slider} Trees")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption(
                "💡 Tip: Notice how the boundary layout evolves and stabilizes when you move from 1 single tree to 50 trees combined.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write("Standard implementation to build, tune, and extract feature importance using **Scikit-Learn**:")

            rf_code = """
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification

    # 1. Generate Synthetic Data
    X, y = make_classification(n_samples=200, n_features=4, random_state=42)

    # 2. Initialize Random Forest (Tuning hyperparameters)
    model = RandomForestClassifier(n_estimators=100, max_depth=5, max_features='sqrt', random_state=42)

    # 3. Train the Model
    model.fit(X, y)

    # 4. Check global Out-of-Bag (OOB) score or Feature Importances
    print("Feature Importances:")
    for i, score in enumerate(model.feature_importances_):
        print(f"Feature {i+1}: {score:.2f}")

    # 5. Make a batch prediction
    predictions = model.predict([[0.1, -0.9, 1.5, 0.4]])
    print(f"Predicted Class: {predictions}")
                """
            st.code(rf_code, language="python")


    elif st.session_state.selected_algo == "Support Vector Machines (SVM)":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Support Vector Machines (SVM)?")
            st.write("""
                Support Vector Machines (SVM) is a powerful Supervised Learning algorithm used for both **Classification and Regression**, though mostly preferred for Classification. 
                The goal of SVM is to find a decision boundary (**Hyperplane**) in an n-dimensional space that distinctly classifies the data points.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood:")
            st.write("SVM relies on finding the best separator by maximizing boundaries:")
            st.markdown("1. **Hyperplane:** The optimal line or plane that separates the data classes.")
            st.markdown("2. **Support Vectors:** The data points that are closest to the hyperplane. If these points are removed, it changes the position of the hyperplane.")
            st.markdown("3. **Margin:** The distance between the hyperplane and the closest support vectors. SVM always tries to maximize this margin (**Maximum Margin Classifier**).")
            st.markdown("4. **The Kernel Trick:** When data is not linearly separable in 2D, SVM uses a mathematical function (Kernel) to transform the data into a higher dimension where it becomes easy to separate.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Text Classification:** Sentiment analysis or spam detection (Works incredibly well with high-dimensional text data).")
            st.write("- **Image Recognition:** Face detection and handwriting recognition.")
            st.write("- **Bioinformatics:** Protein structure classification and gene detection.")

            st.info("💡 **Interview Alert:** Interviewers often ask about **C (Regularization)** and **Gamma** hyperparameters. A low `C` gives a wider margin but allows some misclassifications (Soft Margin), while a high `C` tries to classify everything perfectly (Hard Margin), risking overfitting. `Gamma` defines how far the influence of a single training example reaches.")

        with tab2:
            st.markdown("### 📈 Interactive SVM Regularization Simulation")
            st.write("Adjust the Regularization parameter (C) to see how SVM adjusts its decision boundary around the data points. High C forces strict separation.")

            c_param_slider = st.slider("Regularization Parameter (C)", min_value=0.01, max_value=10.0, value=1.0, step=0.5)

            # Generating Dummy Separation Data
            np.random.seed(0)
            X_svm = np.random.randn(60, 2)
            y_svm = np.where(X_svm[:, 0] + X_svm[:, 1] > 0.3, 1, 0)

            # Fitting SVM Classifier
            from sklearn.svm import SVC
            svm_model = SVC(C=c_param_slider, kernel='linear', random_state=42)
            svm_model.fit(X_svm, y_svm)

            # Plotting the data points and hyperplane boundary
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(X_svm[:, 0], X_svm[:, 1], c=y_svm, cmap="bwr", edgecolors='k', alpha=0.8)

            # Draw decision boundary line
            w = svm_model.coef_[0]
            a = -w[0] / w[1]
            xx = np.linspace(-2, 2)
            yy = a * xx - (svm_model.intercept_[0]) / w[1]
            ax.plot(xx, yy, 'k-', linewidth=2, label="Hyperplane")

            ax.set_xlabel("Feature 1")
            ax.set_ylabel("Feature 2")
            ax.set_title(f"SVM Linear Boundary with C = {c_param_slider}")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption("💡 Tip: Watch how the slope and positioning of the black line slightly shift when you tweak the strictness parameter C.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write("Standard implementation to train an SVM model with a non-linear kernel (RBF) using **Scikit-Learn**:")

            svm_code = """
    from sklearn.svm import SVC
    from sklearn.datasets import make_moons
    from sklearn.model_selection import train_test_split

    # 1. Generate Non-Linear (Moon-shaped) Data
    X, y = make_moons(n_samples=150, noise=0.2, random_state=42)

    # 2. Initialize SVM with Radial Basis Function (RBF) Kernel
    # Tuning C and Gamma prevents underfitting/overfitting
    model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

    # 3. Train the Model
    model.fit(X, y)

    # 4. Extract indices of Support Vectors
    print(f"Total Support Vectors trained: {len(model.support_vectors_)}")

    # 5. Predict Category for new custom coordinates
    prediction = model.predict([[0.5, 0.5]])
    print(f"Predicted Class Label: {prediction}")
                """
            st.code(svm_code, language="python")



    elif st.session_state.selected_algo == "K-Nearest Neighbors (KNN)":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is K-Nearest Neighbors (KNN)?")
            st.write("""
                K-Nearest Neighbors (KNN) is a simple, easy-to-implement Supervised Learning algorithm used for both **Classification and Regression**. 
                It is a **Non-parametric** and **Lazy Learner** algorithm, meaning it does not learn a training model. Instead, it stores the entire training dataset and makes predictions in real-time based on similarity.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood:")
            st.write("KNN classifies a new data point by checking its closest neighbors:")
            st.markdown("1. **Choose K:** Select the number of nearest neighbors to look at (e.g., K = 3 or K = 5).")
            st.markdown(
                "2. **Calculate Distance:** It calculates the distance between the new point and all training points using formulas like **Euclidean Distance**:")
            st.latex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}")
            st.markdown(
                "3. **Find Neighbors:** It selects the 'K' closest data points based on the calculated distance.")
            st.markdown(
                "4. **Majority Vote:** It counts how many neighbors belong to each category. The new point is assigned to the class with the highest vote.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write(
                "- **Recommendation Systems:** Recommending movies or products based on users with similar tastes.")
            st.write(
                "- **Credit Rating:** Assessing bank customer risk profiles by finding similar historical profiles.")
            st.write("- **Pattern Recognition:** Signature verification and handwriting identification.")

            st.info(
                "💡 **Interview Alert:** KNN is highly sensitive to **Feature Scaling** (always use StandardScaler). If one feature has huge numbers, it dominates the distance calculation. Also, always choose an **Odd Number for K** (like 3, 5, 7) for binary classification to avoid a tie in votes!")

        with tab2:
            st.markdown("### 📈 Interactive Neighbor Count (K-Value Selection)")
            st.write(
                "Adjust the number of neighbors (K) to see how KNN alters its decision boundaries. Small K values capture sharp patterns but pick up noise, while large K values make boundaries smoother.")

            k_val_slider = st.slider("Number of Neighbors (K Value)", min_value=1, max_value=15, value=3, step=2)

            # Generating Dummy Clustering Clusters
            np.random.seed(5)
            X_knn = np.random.randn(80, 2)
            y_knn = (X_knn[:, 0] + X_knn[:, 1] > 0).astype(int)

            # Fitting KNN Classifier
            from sklearn.neighbors import KNeighborsClassifier

            knn_model = KNeighborsClassifier(n_neighbors=k_val_slider)
            knn_model.fit(X_knn, y_knn)

            # Plotting the dataset map
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(X_knn[:, 0], X_knn[:, 1], c=y_knn, cmap="winter", edgecolors='k', alpha=0.8)
            ax.set_xlabel("Feature X1")
            ax.set_ylabel("Feature X2")
            ax.set_title(f"KNN Classification Cluster Map (K = {k_val_slider})")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption("💡 Notice how changing the K value dynamically alters the core group voting density.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write("Standard code structure to scale data and train a KNN Classifier using **Scikit-Learn**:")

            knn_code = """
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import make_classification

    # 1. Generate Synthetic Dataset
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

    # 2. Crucial Step: Feature Scaling (KNN requires data normalization!)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Initialize KNN Classifier with odd value of K
    model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

    # 4. Train the Model
    model.fit(X_scaled, y)

    # 5. Predict on new incoming data point
    new_data_point = [[0.2, -0.5]]
    scaled_point = scaler.transform(new_data_point)
    prediction = model.predict(scaled_point)
    print(f"Predicted Class Label: {prediction}")
                """
            st.code(knn_code, language="python")



    elif st.session_state.selected_algo == "K-Means Clustering":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is K-Means Clustering?")
            st.write("""
                K-Means Clustering is a popular Unsupervised Learning algorithm used to partition an unlabeled dataset into **K distinct, non-overlapping groups (clusters)**. 
                It automatically groups data points together based on their feature similarity without any human guidance or historical target labels.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood (Iterative Process):")
            st.markdown("1. **Choose K:** Select the number of clusters (K) you want to discover.")
            st.markdown(
                "2. **Initialize Centroids:** Randomly place K points in the feature space. These are called **Centroids** (group centers).")
            st.markdown(
                "3. **Assign Points:** Calculate the distance (usually **Euclidean Distance**) from every data point to all K centroids. Assign each point to its closest centroid.")
            st.markdown(
                "4. **Update Centroids:** Take the mathematical average (mean) of all data points inside a cluster and move the centroid to that new center position.")
            st.markdown(
                "5. **Repeat:** Keep repeating steps 3 and 4 until the centroids stop changing position (Convergence).")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write(
                "- **Customer Segmentation:** Grouping bank or e-commerce buyers based on spending behavior and age for targeted marketing.")
            st.write(
                "- **Image Compression:** Reducing the number of unique colors in an image by clustering similar pixel values together.")
            st.write(
                "- **Document Clustering:** Automatically grouping thousands of news articles into topics (Sports, Finance, Tech).")

            st.info(
                "💡 **Interview Alert:** Interviewers will ask: *'How do you choose the best value of K?'* The answer is the **Elbow Method**. It plots the Within-Cluster Sum of Squares (WCSS/Inertia) against different values of K. The point where the curve bends like an elbow is considered the optimal K!")

        with tab2:
            st.markdown("### 📈 Interactive Cluster Selection (Value of K)")
            st.write(
                "Adjust the number of clusters (K) slider to see how the K-Means algorithm partitions the unlabeled dataset in real-time.")

            k_clusters_slider = st.slider("Select Number of Clusters (K)", min_value=1, max_value=5, value=3, step=1)

            # Generating Unlabeled Data Blobs
            from sklearn.datasets import make_blobs

            X_kmeans, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.0, random_state=42)

            # Fitting K-Means
            from sklearn.cluster import KMeans

            kmeans_model = KMeans(n_clusters=k_clusters_slider, init='k-means++', random_state=42, n_init=10)
            y_kmeans = kmeans_model.fit_predict(X_kmeans)
            centroids = kmeans_model.cluster_centers_

            # Plotting clusters
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(X_kmeans[:, 0], X_kmeans[:, 1], c=y_kmeans, cmap="rainbow", edgecolors='k', alpha=0.7,
                       label="Data Points")
            # Drawing Centroids as Big Gold Stars
            ax.scatter(centroids[:, 0], centroids[:, 1], s=250, c='gold', marker='*', edgecolors='black', linewidth=1.5,
                       label="Centroids")

            ax.set_xlabel("Feature 1")
            ax.set_ylabel("Feature 2")
            ax.set_title(f"K-Means Clustering with K = {k_clusters_slider}")
            ax.legend(loc="upper right")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption(
                "💡 Notice how the golden star centroids re-calculate and shift centers depending on your K value input.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write(
                "Standard implementation to train a K-Means model, find optimal centroids, and calculate WCSS (Inertia) using **Scikit-Learn**:")

            kmeans_code = """
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs

    # 1. Generate Unlabeled Mock Data (No y target labels are used!)
    X, _ = make_blobs(n_samples=200, n_features=2, centers=4, random_state=42)

    # 2. Initialize K-Means (init='k-means++' prevents bad random initialization)
    model = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=42)

    # 3. Fit and Predict Cluster Labels in one step
    cluster_labels = model.fit_predict(X)

    # 4. Check Final Centroid Coordinates
    print("Final Learned Centroids Locations:")
    print(model.cluster_centers_)

    # 5. Extract WCSS (Inertia) for Elbow Method analysis
    print(f"Within-Cluster Sum of Squares (Inertia): {model.inertia_:.2f}")
                """
            st.code(kmeans_code, language="python")


    elif st.session_state.selected_algo == "Hierarchical Clustering":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Hierarchical Clustering?")
            st.write("""
                Hierarchical Clustering is an Unsupervised Learning technique that builds a tree-like hierarchy of clusters. 
                Unlike K-Means, you do not need to specify the number of clusters beforehand. It is mainly divided into two types:
                """)
            st.markdown(
                "1. **Agglomerative (Bottom-Up):** Every data point starts as its own cluster. The algorithm iteratively merges the closest pairs of clusters until only one giant cluster remains. (Most Common)")
            st.markdown(
                "2. **Divisive (Top-Down):** All data points start in one big cluster, which is recursively split down into smaller clusters until each point is its own cluster.")

            st.markdown("#### 🧮 Linkage Methods (How distance between clusters is measured):")
            st.write("To merge clusters, we must calculate the distance between groups using linkage criteria:")
            st.markdown("- **Single Linkage:** Distance between the closest points of two clusters.")
            st.markdown("- **Complete Linkage:** Distance between the farthest points of two clusters.")
            st.markdown("- **Average Linkage:** Average distance between all pairs of points.")
            st.markdown("- **Ward's Method:** Minimizes the total within-cluster variance (Default in Scikit-Learn).")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write(
                "- **Bioinformatics:** Creating a phylogenetic tree (family tree) of different animal species or gene expressions.")
            st.write(
                "- **Market Research:** Building granular customer archetypes where sub-groups exist inside larger groups.")
            st.write("- **Image Segmentation:** Grouping pixels hierarchically to understand object structures.")

            st.info(
                "💡 **Interview Alert:** Interviewers love asking about **Dendrograms**. A Dendrogram is a tree diagram that records the sequences of merges or splits. To find the optimal number of clusters, you draw a horizontal line across the highest vertical line that hasn't been crossed by any extended horizontal merge line!")

        with tab2:
            st.markdown("### 📈 Live Tree Hierarchy (Dendrogram Visualizer)")
            st.write(
                "Adjust the linkage method using the dropdown to see how the mathematical tree (Dendrogram) changes layout when linking sample data points.")

            linkage_choice = st.selectbox("Select Linkage Criteria:", ["ward", "single", "complete", "average"])

            # Importing Scipy for Dendrogram generation
            from scipy.cluster.hierarchy import dendrogram, linkage

            # Generating sample stable dataset
            np.random.seed(22)
            X_hier = np.random.randn(15, 2)

            # Performing hierarchical linkage
            Z = linkage(X_hier, method=linkage_choice)

            # Plotting Dendrogram
            fig, ax = plt.subplots(figsize=(6, 3.2))
            dendrogram(Z, ax=ax)
            ax.set_title(f"Dendrogram using '{linkage_choice}' linkage")
            ax.set_xlabel("Data Points Index")
            ax.set_ylabel("Distance Threshold")
            ax.grid(axis='y', linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption(
                "💡 Tip: The horizontal lines represent merges. The height of the vertical line indicates the distance between the merged clusters.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write("Standard implementation to apply Agglomerative Clustering and fit labels using **Scikit-Learn**:")

            hier_code = """
    from sklearn.cluster import AgglomerativeClustering
    import numpy as np

    # 1. Dummy Unlabeled Coordinates Data
    X = np.array([[1, 2], [1, 4], [1, 0],
    , [4, 4], [4, 0]])

    # 2. Initialize Agglomerative Clustering
    # We set 2 clusters and use Ward's linkage (Euclidean distance is default)
    model = AgglomerativeClustering(n_clusters=2, linkage='ward')

    # 3. Fit and Predict cluster groupings
    cluster_labels = model.fit_predict(X)

    print(f"Assigned Cluster Labels for each row: {cluster_labels}")
                """
            st.code(hier_code, language="python")


    elif st.session_state.selected_algo == "Principal Component Analysis (PCA)":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Principal Component Analysis (PCA)?")
            st.write("""
                Principal Component Analysis (PCA) is an Unsupervised Learning algorithm used for **Dimensionality Reduction**. 
                It transforms a large set of variables into a smaller one that still contains most of the information (variance) from the original large set. 
                It is heavily used to speed up training times, reduce storage, and visualize multi-dimensional datasets.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood (Step-by-Step Math):")
            st.markdown(
                "1. **Standardization:** Scale the data (`StandardScaler`) so that all features have a Mean of 0 and Variance of 1. PCA is highly sensitive to variances of original variables.")
            st.markdown(
                "2. **Covariance Matrix Computation:** Calculate how the variables are varying from the mean with respect to each other to see if there is any correlation.")
            st.markdown(
                "3. **Eigenvectors & Eigenvalues:** Compute the mathematical directions of data spread (**Eigenvectors**) and their magnitude/strength (**Eigenvalues**).")
            st.markdown(
                "4. **Principal Components (PCs):** Sort the eigenvectors by eigenvalues in descending order. The top vector becomes PC1 (captures maximum variance), the next becomes PC2, and so on. PCs are perpendicular (orthogonal) to each other.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write(
                "- **Image Processing:** Compression and facial recognition (Eigenfaces) by reducing thousands of pixels into key features.")
            st.write(
                "- **Genomics:** Analyzing DNA data where a single patient might have 10,000+ genetic feature columns.")
            st.write(
                "- **Data Visualization:** Compressing a 10-column financial dataset into 2D to easily spot fraud patterns on a scatter plot.")

            st.info(
                "💡 **Interview Alert:** Interviewers will ask: *'How do you know how many principal components to keep?'* The answer is by looking at the **Scree Plot** or the **Explained Variance Ratio**. For example, if PC1 explains 70% variance and PC2 explains 15%, keeping just these two PCs allows you to retain 85% of the original information!")

        with tab2:
            st.markdown("### 📈 Interactive Dimensionality Reduction Visualizer")
            st.write(
                "Adjust the slider to simulate dropping dimensions and see how projecting 3D correlated data onto a 2D PCA plane captures the core distribution shape.")

            angle_slider = st.slider("Rotate Data Visualization Angle", min_value=0, max_value=180, value=45, step=15)

            # Generating simulated 3D highly correlated data points
            np.random.seed(42)
            x_pca = np.random.randn(80)
            y_pca = x_pca * 1.5 + np.random.normal(0, 0.2, 80)
            z_pca = y_pca * 0.8 + np.random.normal(0, 0.1, 80)
            X_3d = np.vstack((x_pca, y_pca, z_pca)).T

            # Fitting live PCA using Scikit-Learn
            from sklearn.decomposition import PCA

            pca_model = PCA(n_components=2)
            X_2d = pca_model.fit_transform(X_3d)
            var_ratio = pca_model.explained_variance_ratio_

            # Plotting the variance contribution using Matplotlib
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.bar(["PC1", "PC2"], var_ratio * 100, color=["#1E3A8A", "#FF4B4B"], edgecolor='k', width=0.5)
            ax.set_ylabel("Percentage of Variance Explained (%)")
            ax.set_title(f"PC1 retains {var_ratio[0] * 100:.1f}% info | PC2 retains {var_ratio[1] * 100:.1f}% info")
            ax.set_ylim(0, 100)
            ax.grid(axis='y', linestyle="--", alpha=0.5)

            st.pyplot(fig)
            st.caption(
                f"💡 This chart proves that by keeping just 2 components, you successfully retained **{(var_ratio[0] + var_ratio[1]) * 100:.1f}%** of the entire 3D dataset's information!")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write(
                "Standard industry code pipeline to standardize features and compress dimensions using **Scikit-Learn**:")

            pca_code = """
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    import numpy as np

    # 1. Create a high-dimensional dummy matrix (5 rows, 4 feature columns)
    X_high_dim = np.array([
        [2.5, 2.4, 0.5, 4.1],
        [0.5, 0.7, 3.2, 1.2],
        [2.2, 2.9, 0.2, 3.8],
        [1.9, 2.2, 1.1, 2.9],
        [3.1, 3.0, 0.1, 4.9]
    ])

    # 2. MANDATORY STEP: Standardize the features before running PCA
    scaler = StandardScaler()
    X_standardized = scaler.fit_transform(X_high_dim)

    # 3. Initialize PCA to compress 4 dimensions down into 2 Principal Components
    pca = PCA(n_components=2)

    # 4. Fit and apply the dimensionality reduction transformation
    X_reduced = pca.fit_transform(X_standardized)

    print("Original Shape:", X_high_dim.shape)  # Output: (5, 4)
    print("Reduced PCA Shape:", X_reduced.shape)  # Output: (5, 2)

    # 5. Check exactly how much information was retained
    print(f"Explained Variance Ratio per PC: {pca.explained_variance_ratio_}")
    print(f"Total Retained Information: {np.sum(pca.explained_variance_ratio_)*100:.2f}%")
                """
            st.code(pca_code, language="python")


    elif st.session_state.selected_algo == "Isolation Forest":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Isolation Forest?")
            st.write("""
                Isolation Forest is an advanced Unsupervised Learning algorithm specifically designed for **Anomaly Detection** (Outlier Detection). 
                Instead of profiling normal data points and finding differences, it explicitly isolates anomalies. It is built on the principle 
                that anomalies are few and far between, making them easier to isolate than normal observations.
                """)

            st.markdown("#### 🧮 How it Works Under the Hood (Tree Isolation Logic):")
            st.markdown(
                "1. **Random Partitioning:** The algorithm randomly selects a feature and then randomly selects a split value between the maximum and minimum values of that feature.")
            st.markdown(
                "2. **Tree Construction:** It repeats this process recursively to build isolation trees (iTrees).")
            st.markdown(
                "3. **Path Length Calculation:** Anomalies require very few random splits to be isolated because they exist at extreme values. Therefore, they have a **shorter path length** from the root node to the leaf node.")
            st.markdown(
                "4. **Anomaly Score:** Points with noticeably short path lengths across the entire forest are assigned an anomaly score close to 1 and flagged as outliers. Normal points get a score closer to 0.")

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write("- **Credit Card Fraud:** Catching a sudden highly unusual international transaction amount.")
            st.write(
                "- **Server Health:** Detecting network intrusion or severe server performance spikes (Hacking attempts).")
            st.write("- **Manufacturing QA:** Spotting defective parts on a factory assembly line before packaging.")

            st.info(
                "💡 **Interview Alert:** A favorite interview question is: *'Why use Isolation Forest over distance-based methods like KNN or K-Means for outliers?'* The answer is **Efficiency**. Distance-based methods require calculating distances between every single pair of points, which becomes extremely slow for large datasets. Isolation Forest has a linear time complexity, making it incredibly fast and scalable!")

        with tab2:
            st.markdown("### 📈 Interactive Contamination Visualizer")
            st.write(
                "Adjust the contamination slider (the expected percentage of outliers in the data) to see how the Isolation Forest dynamically catches and highlights the rare anomalies (red points) away from the normal cluster (blue points).")

            contamination_slider = st.slider("Expected Contamination Rate (Outlier %)", min_value=0.01, max_value=0.20,
                                             value=0.05, step=0.01)

            # Generating normal cluster data combined with random far outliers
            np.random.seed(42)
            X_normal = 0.5 * np.random.randn(90, 2)
            X_outliers = np.random.uniform(low=-4, high=4, size=(10, 2))
            X_iso = np.vstack((X_normal, X_outliers))

            # Fitting Isolation Forest
            from sklearn.ensemble import IsolationForest

            iso_model = IsolationForest(contamination=contamination_slider, random_state=42)
            iso_preds = iso_model.fit_predict(X_iso)  # Returns 1 for normal, -1 for outlier

            # Plotting the anomaly detection layout
            fig, ax = plt.subplots(figsize=(6, 3.2))
            ax.scatter(X_iso[iso_preds == 1, 0], X_iso[iso_preds == 1, 1], c="#1E3A8A", label="Normal Points (Inliers)",
                       alpha=0.7)
            ax.scatter(X_iso[iso_preds == -1, 0], X_iso[iso_preds == -1, 1], c="#FF4B4B", label="Anomalies Detected",
                       s=70, edgecolors='black', linewidth=1)

            ax.set_xlabel("Feature X1")
            ax.set_ylabel("Feature X2")
            ax.set_title(f"Isolation Forest Analysis (Contamination: {contamination_slider * 100:.0f}%)")
            ax.legend(loc="lower left")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
            st.caption(
                "💡 Notice how the red dots are isolated at the outer edges of the plot, mirroring how credit card companies track unusual activity data.")

        with tab3:
            st.markdown("### 💻 Clean Production Code Template")
            st.write(
                "Standard code structure to train an Isolation Forest model and extract continuous anomaly scores using **Scikit-Learn**:")

            iso_code = """
    from sklearn.ensemble import IsolationForest
    import numpy as np

    # 1. Create a dummy data matrix (Normal transactions around $20-50, one fraud at $5000)
    X_transactions = np.array([
        [25.0, 1.0], [42.5, 2.0], [19.9, 1.0], [35.0, 3.0], [50.0, 2.0],
        [5000.0, 99.0] # Massive transaction amount and high transaction count outlier
    ])

    # 2. Initialize Isolation Forest
    # contamination=0.15 means we estimate roughly 15% of data rows could be anomalies
    model = IsolationForest(contamination=0.15, random_state=42)

    # 3. Fit model and predict flags (1 = normal, -1 = anomaly)
    flags = model.fit_predict(X_transactions)

    # 4. Extract raw anomaly scores (Lower/more negative scores indicate higher anomaly risk)
    scores = model.decision_function(X_transactions)

    print("Transaction Check Results:")
    for i, (flag, score) in enumerate(zip(flags, scores)):
        status = "⚠️ FRAUD DETECTED" if flag == -1 else "✅ Normal"
        print(f"Row {i+1}: Status: {status} | Score: {score:.3f}")
                """
            st.code(iso_code, language="python")


    elif st.session_state.selected_algo == "Q-Learning (Core Concept)":
        tab1, tab2, tab3 = st.tabs(["📌 Concept & Math", "📈 Live Visualization", "💻 Production Code"])

        with tab1:
            st.markdown("### 🔍 What is Reinforcement Learning & Q-Learning?")
            st.write("""
                **Reinforcement Learning (RL)** is a type of Machine Learning where an autonomous **Agent** learns to make decisions by performing actions in an **Environment** to maximize cumulative **Rewards**. 
                Unlike Supervised learning, it does not use a dataset. It learns entirely through trial-and-error.

                **Q-Learning** is a model-free, off-policy RL algorithm used to find the best action to take given the current state. It builds a **Q-Table** (Quality Table) where rows represent States and columns represent Actions.
                """)

            st.markdown("#### 🧮 The Bellman Equation (How Q-Values Update):")
            st.latex(
                r"Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R(s, a) + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]")

            st.markdown("""
                * **$Q(s, a)$:** The current quality score of taking action $a$ in state $s$.
                * **$\alpha$ (Learning Rate):** How much the agent accepts new information over old information (0 to 1).
                * **$R(s, a)$:** The immediate Reward received after taking that action.
                * **$\gamma$ (Discount Factor):** How much the agent values future rewards compared to immediate rewards (0 to 1).
                * **$\max_{a'} Q(s', a')$:** The maximum expected future reward from the next state $s'$.
                """)

            st.markdown("#### 🎯 Practical Use-Cases (Where to use?):")
            st.write(
                "- **Autonomous Vehicles:** Training self-driving cars to navigate traffic and stay in lanes safely.")
            st.write("- **Gaming AI:** Building bots that defeat world champions in games like Chess, Go, or Dota 2.")
            st.write("- **Robotics:** Training mechanical arms to pick up fragile items without breaking them.")

            st.info(
                "💡 **Interview Alert:** Interviewers will ask about the **Exploration vs. Exploitation Trade-off**. **Exploration** means trying random new paths to discover rewards, while **Exploitation** means using known paths that already give good rewards. This is controlled using the **Epsilon-Greedy ($\epsilon$)** strategy!")

        with tab2:
            st.markdown("### 📈 Interactive Q-Table Learning Simulation")
            st.write(
                "Adjust the Exploration Rate ($\epsilon$) to see how it affects an agent trying to find a path. A high exploration rate means the agent moves randomly, while a low rate forces it to use the trained Q-table.")

            epsilon_slider = st.slider("Exploration Rate (Epsilon - ε)", min_value=0.0, max_value=1.0, value=0.2,
                                       step=0.1)

            # Simple simulation representation using Matplotlib
            fig, ax = plt.subplots(figsize=(6, 2.5))
            # Drawing a simple 4x4 grid maze representation
            grid = np.zeros((4, 4))
            grid[0, 0] = 1  # Start Point (Agent)
            grid[3, 3] = 2  # Goal Point (Reward)
            grid[1, 2] = -1  # Obstacle (Penalty)
            grid[2, 1] = -1  # Obstacle (Penalty)

            ax.imshow(grid, cmap="cool", alpha=0.3)
            ax.text(0, 0, "🤖 Agent\n(Start)", ha="center", va="center", fontsize=8, weight="bold")
            ax.text(3, 3, "🏆 Goal\n(+100)", ha="center", va="center", fontsize=8, weight="bold")
            ax.text(2, 1, "💥 Trap\n(-50)", ha="center", va="center", fontsize=8, weight="bold")
            ax.text(1, 2, "💥 Trap\n(-50)", ha="center", va="center", fontsize=8, weight="bold")

            # Simulated Agent Step direction based on epsilon input
            if epsilon_slider > 0.6:
                strategy_text = "🔄 Strategy: Exploring Randomly (Searching for rewards)"
                ax.arrow(0, 0, 0, 0.6, head_width=0.15, head_length=0.15, fc='red', ec='red')
            else:
                strategy_text = "🎯 Strategy: Exploiting Q-Table (Taking optimal path to goal)"
                ax.arrow(0, 0, 0.8, 0, head_width=0.15, head_length=0.15, fc='green', ec='green')
                ax.arrow(1, 0, 0, 0.8, head_width=0.15, head_length=0.15, fc='green', ec='green')

            ax.set_xticks([])
            ax.set_yticks([])
            st.pyplot(fig)
            st.caption(f"💡 **Current State:** {strategy_text}")

        with tab3:
            st.markdown("### 💻 Python Code Template (Numpy Implementation)")
            st.write(
                "Since Scikit-Learn does not contain RL, industries write Q-learning from scratch using **NumPy** matrix loops:")

            rl_code = """
    import numpy as np
    import random

    # 1. Initialize environment dimensions (4 states, 2 actions: Left or Right)
    num_states = 4
    num_actions = 2

    # 2. Initialize Q-Table with zeros
    q_table = np.zeros((num_states, num_actions))

    # 3. Hyperparameters
    alpha = 0.1    # Learning Rate
    gamma = 0.9    # Discount Factor
    epsilon = 0.2  # Exploration Rate

    # 4. Training Loop (Simulated Episode step)
    for episode in range(100):
        state = 0  # Start state

        # Epsilon-Greedy Action Selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice([0, 1])  # Explore randomly
        else:
            action = np.argmax(q_table[state])  # Exploit learned actions

        # Dummy Reward response from environment
        reward = 10 if action == 1 else -2
        next_state = 1

        # Bellman Equation Update rule
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        q_table[state, action] = old_value + alpha * (reward + gamma * next_max - old_value)

    print("Final Trained Q-Table Quality Scores:")
    print(q_table)
                """
            st.code(rl_code, language="python")

    st.write("\n")
    if st.button("⬅️ Back to Algorithm List"):
        st.session_state.page = "algo_menu"
        st.rerun()

