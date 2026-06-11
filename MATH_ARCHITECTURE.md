# 📐 ASTRIA: Mathematical Architecture (V2)

The fundamental flaw of naive collision avoidance is treating satellites as point masses in a static 3D grid. ASTRIA V2 implements a probabilistic approach.

## 1. Covariance in the RTN Frame
Given a satellite's state vector derived from a TLE, we assign an empirical uncertainty matrix in the Radial, Transverse, Normal (RTN) frame:
$$C_{RTN} = \begin{bmatrix} \sigma_R^2 & 0 & 0 \\ 0 & \sigma_T^2 & 0 \\ 0 & 0 & \sigma_N^2 \end{bmatrix}$$
*Where $\sigma_T$ (Along-track error) dominates due to atmospheric drag uncertainties.*

## 2. B-Plane Projection
At the Time of Closest Approach (TCA), the relative velocity is extremely high (e.g., $15$ km/s). We project the combined 3D covariance $C_{combined}$ onto a 2D encounter plane (the B-Plane) orthogonal to the relative velocity $v_{rel}$.

## 3. Probability of Collision ($P_c$)
The collision probability is the integral of the 2D Gaussian probability density function over the combined Hardbody Radius (HBR) of the two satellites:
$$P_c = \frac{1}{2\pi \sqrt{|C_p|}} \iint_{A} \exp\left(-\frac{1}{2} r^T C_p^{-1} r\right) dx dy$$

## 4. Mahalanobis Distance as an AI Feature
Instead of feeding Euclidean distance $\Delta r$ to the XGBoost model, ASTRIA V2 utilizes the Mahalanobis distance ($D_M$), which scales the miss vector $\mu$ by the inverse of the covariance matrix:
$$D_M = \sqrt{\mu^T C_p^{-1} \mu}$$
This allows the AI to distinguish between a "close-but-certainly-safe" pass and a "distant-but-highly-uncertain" threat.
